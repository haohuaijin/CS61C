/*********************
**  Mandelbrot fractal movie generator
** clang -Xpreprocessor -fopenmp -lomp -o Mandelbrot Mandelbrot.c
** by Dan Garcia <ddgarcia@cs.berkeley.edu>
** Modified for this class by Justin Yokota and Chenyu Shi
**********************/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include "ComplexNumber.h"
#include "Mandelbrot.h"
#include "ColorMapInput.h"
#include <sys/types.h>

void printUsage(char* argv[])
{
  printf("Usage: %s <threshold> <maxiterations> <center_real> <center_imaginary> <initialscale> <finalscale> <framecount> <resolution> <output_folder> <colorfile>\n", argv[0]);
  printf("    This program simulates the Mandelbrot Fractal, and creates an iteration map of the given center, scale, and resolution, then saves it in output_file\n");
}


/*
This function calculates the threshold values of every spot on a sequence of frames. The center stays the same throughout the zoom. First frame is at initialscale, and last frame is at finalscale scale.
The remaining frames form a geometric sequence of scales, so 
if initialscale=1024, finalscale=1, framecount=11, then your frames will have scales of 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1.
As another example, if initialscale=10, finalscale=0.01, framecount=5, then your frames will have scale 10, 10 * (0.01/10)^(1/4), 10 * (0.01/10)^(2/4), 10 * (0.01/10)^(3/4), 0.01 .
*/
void MandelMovie(double threshold, long max_iterations, ComplexNumber* center, double initialscale, double finalscale, int framecount, long resolution, long ** output){
    //YOUR CODE HERE
	for(int i=0; i<framecount; i++){
		double scale = initialscale * pow((double)finalscale / (double)initialscale, (double)i / (double)(framecount-1));
		printf("%lf\n", scale);
		Mandelbrot(threshold, max_iterations, center, scale, resolution, output[i]);
	}	
}

/**************
**This main function converts command line inputs into the format needed to run MandelMovie.
**It then uses the color array from FileToColorMap to create PPM images for each frame, and stores it in output_folder
***************/
int main(int argc, char* argv[])
{
	//Tips on how to get started on main function: 
	//MandelFrame also follows a similar sequence of steps; it may be useful to reference that.
	//Mayke you complete the steps below in order. 

	//STEP 1: Convert command line inputs to local variables, and ensure that inputs are valid.
	/*
	Check the spec for examples of invalid inputs.
	Remember to use your solution to B.1.1 to process colorfile.
	*/

	//YOUR CODE HERE 
	if(argc != 11) {
		printf("%s: Wrong number of arguments, expecting 7\n", argv[0]);
		printUsage(argv);
		return 1;
	}
	double threshold,initialscale, finalscale;
	int framecount;
	ComplexNumber* center;
	long max_iterations, resolution;

	threshold = atof(argv[1]);
	max_iterations = (long)atoi(argv[2]);
	center = newComplexNumber(atof(argv[3]), atof(argv[4]));
	initialscale = atof(argv[5]);
	finalscale = atof(argv[6]);
	framecount = (int)atoi(argv[7]);
	resolution = (long)atoi(argv[8]);

	if(threshold <= 0 || initialscale <= 0 || finalscale <= 0 || max_iterations <= 0){
		printf("The threshold, initscale, finalscale, max_iterations must be > 0\n");
		printUsage(argv);
		return 1;
	}
	if(resolution < 0){
		printf("The resolution must be >= 0\n");
		printUsage(argv);
		return 1;
	}
	if(framecount > 10000 || framecount <= 0){
		printf("The framecount must in the range of (0, 10000)\n");
		printUsage(argv);
		return 1;
	}
	if(framecount == 1 && initialscale != finalscale){
		printf("The framecount is not 1\n");
		printUsage(argv);
		return 1;
	}
	//get the colormap and color num
	int *colorcount = (int*)malloc(sizeof(int));
	int **colormap = FileToColorMap(argv[10], colorcount);


	//STEP 2: Run MandelMovie on the correct arguments.
	/*
	MandelMovie requires an output array, so make sure you allocate the proper amount of space. 
	If allocation fails, free all the space you have already allocated (including colormap), then return with exit code 1.
	*/

	//YOUR CODE HERE 
	int len = 2 * resolution + 1;
	long **output;
	output = (long**)malloc(framecount * sizeof(long*));
	if(output == NULL){
		printf("Unable to allocate **output\n");
		return 1;
	}
	for(int i=0; i<framecount; i++){
		output[i] = (long*)malloc(sizeof(long) * len * len);
		if(output[i] == NULL){
			printf("Unable to malloc \n");
			return 1;
		}
	}

	MandelMovie(threshold, max_iterations, center, initialscale, finalscale, framecount, resolution, output);
	
	/*
	printf("**************************************\n");
	for(int i=0; i<framecount; i++){
		for(int j=0; j<len*len; j++){
			printf("%ld ", output[i][j]);
		}
		printf("\n");
	}
	printf("**************************************\n\n");
	*/

	//STEP 3: Output the results of MandelMovie to .ppm files.
	/*
	Convert from iteration count to colors, and output the results into output files.
	Use what we showed you in Part B.1.2, create a seqeunce of ppm files in the output folder.
	Feel free to create your own helper function to complete this step.
	As a reminder, we are using P6 format, not P3.
	*/

	//YOUR CODE HERE 
	//argv[9] is the output_foler
	// colormap, colorcount, output, framecount.
	for(int i=0; i<framecount; i++){
		char a[35];
		sprintf(a, "%s/frame%05d.ppm", argv[9], i); 	//低级错误 把i写成了framecount
		FILE *out = fopen(a, "w");
		fprintf(out, "P6 %d %d 255\n", len, len); 		//忘了加\n
		for(int m=0; m<len*len; m++){
			if(output[i][m] == 0){ 						//haha, lowest error 低级错误 把i写成了framecount
				fprintf(out, "%c%c%c", 0, 0, 0); 
			} else {
				int index = ((int)output[i][m]-1) % (*colorcount);
				fprintf(out, "%c%c%c", colormap[index][0], colormap[index][1], colormap[index][2]);
			}
			
		}
		fclose(out);
	}


	//STEP 4: Free all allocated memory
	/*
	Make sure there's no memory leak.
	*/
	//YOUR CODE HERE 
	for(int i=0; i<framecount; i++){
		free(output[i]);
	}
	free(output);




	return 0;
}

