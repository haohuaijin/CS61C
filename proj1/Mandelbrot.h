/*********************
**  Mandelbrot fractal
** clang -Xpreprocessor -fopenmp -lomp -o Mandelbrot Mandelbrot.c
** by Dan Garcia <ddgarcia@cs.berkeley.edu>
** Modified for this class by Justin Yokota and Chenyu Shi
**********************/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

/*
This function returns the number of iterations that cause the initial point to exceed the threshold.
If the threshold is not exceeded after maxiters, the function returns maxiters.
*/
long MandelbrotIterations(long maxiters, ComplexNumber * point, double threshold);

/*
This function calculates the Mandelbrot plot and stores the result in output.
The number of pixels in the image is resolution * 2 + 1 in one row/column. It's a square image.
Scale is the the distance between center and the top pixel in one dimension.
*/
void Mandelbrot(double threshold, long max_iterations, ComplexNumber* center, double scale, long resolution, long * output);
