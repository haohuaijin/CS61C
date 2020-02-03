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

/*
This function returns the number of iterations before the initial point >= the threshold.
If the threshold is not exceeded after maxiters, the function returns 0.
*/
long MandelbrotIterations(long maxiters, ComplexNumber * point, double threshold)
{
    //YOUR CODE HERE
	ComplexNumber *Z = newComplexNumber(0.0, 0.0);
	ComplexNumber *C = point;
	for(int i = 1; i <= maxiters; i++){
		ComplexNumber *powZ = ComplexProduct(Z, Z);
		free(Z);
		Z = ComplexSum(powZ, C);
		free(powZ);
		if(ComplexAbs(Z) >= threshold){
			free(Z);
			free(C);
			return i;
		}
	}
	free(Z);
	free(C);
	return 0;
}

/*
This function calculates the Mandelbrot plot and stores the result in output.
The number of pixels in the image is resolution * 2 + 1 in one row/column. It's a square image.
Scale is the the distance between center and the top pixel in one dimension.
*/
void Mandelbrot(double threshold, long max_iterations, ComplexNumber* center, double scale, long resolution, long * output){
    //YOUR CODE HERE
	double dis = scale/resolution;
	int len = resolution*2 + 1;
	int count = 0;
	for(int m = 0; m < len; m++){
		for(int j = 0; j < len; j++){
			double re = Re(center) + dis*(j-resolution);
			double im = Im(center) - dis*(m-resolution);
			ComplexNumber *C = newComplexNumber(re, im);
			output[count++] = MandelbrotIterations(max_iterations, C, threshold);
			//free(C);
		}
	}
}
















