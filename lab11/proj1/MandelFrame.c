/*********************
**  Mandelbrot fractal
** clang -Xpreprocessor -fopenmp -lomp -o Mandelbrot Mandelbrot.c
** by Dan Garcia <ddgarcia@cs.berkeley.edu>
** Modified for this class by Justin Yokota and Chenyu Shi
**********************/

#include <stdio.h>
#include <stdlib.h>
#include "ComplexNumber.h"
#include "Mandelbrot.h"
#include <sys/types.h>

void printUsage(char* argv[])
{
  printf("Usage: %s <threshold> <maxiterations> <center_real> <center_imaginary> <scale> <resolution> <output_file>\n", argv[0]);
  printf("    This program simulates the Mandelbrot Fractal, and creates an iteration map of the given center, scale, and resolution, then saves it in output_file\n");
}

	/**************
	**This main function converts command line inputs into the format needed to run Mandelbrot.
	**It also stores the result of Mandelbrot in the input file of your choice.
	**We have hidden one memory leak in this code that you will need to fix. Yes, we are evil.
	***************/
	int main(int argc, char* argv[])
{
	test_complex_number();

	//STEP 1: Convert command line inputs to local variables, and ensure that inputs are valid.
	// Check number of args
	if (argc != 8) {
		printf("%s: Wrong number of arguments, expecting 7\n", argv[0]);
		printUsage(argv);
		return 1;
	}
	double threshold, scale;
	ComplexNumber* center;
	u_int64_t max_iterations, resolution;

	threshold = atof(argv[1]);
	max_iterations = (u_int64_t)atoi(argv[2]);
	center = newComplexNumber(atof(argv[3]), atof(argv[4]));
	scale = atof(argv[5]);
	resolution = (u_int64_t)atoi(argv[6]);

	if (threshold <= 0 || scale <= 0 || max_iterations <= 0) {
		printf("The threshold, scale, and max_iterations must be > 0");
		printUsage(argv);
		return 1;
	}
	u_int64_t size = 2 * resolution + 1;
	//END STEP 1

	//STEP 2: Run Mandelbrot on the correct arguments.
	u_int64_t *ar;
	ar = (u_int64_t *)malloc(size * size * sizeof(u_int64_t));
	if (ar == NULL) {
		printf("Unable to allocate %lu bytes\n", size * size * sizeof(u_int64_t));
		return 1;
	}
	printf("Beginning calculation of Mandelbrot grid centered on %lf + %lfi, with scale of %lf, max iterations of %lu, \nthreshold of %lf, and resolution of %lu \n",
		atof(argv[3]), atof(argv[4]), scale, max_iterations, threshold, resolution);

	Mandelbrot(threshold, max_iterations, center, scale, resolution, ar);

	printf("Calculation complete, outputting to file %s\n", argv[7]);
	//END STEP 2

	//STEP 3: Output the results of Mandelbrot to .txt files.
	FILE* outputfile = fopen(argv[7], "w+");
	u_int64_t iterations;
	for (int row = 0; row < size; row++) {
		for (int col = 0; col < size; col++) {
			iterations = *(ar + row*size + col); // ar[row][col];

			fprintf(outputfile, "%lu ", iterations);
		}
		fputc('\n', outputfile);
	}	
	
	fclose(outputfile);

	//END STEP 3

	//STEP 4: Free all allocated memory
	free(ar);
	return 0;
}
