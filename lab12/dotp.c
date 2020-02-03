#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

#define ARRAY_SIZE 10000000
#define REPEAT     100

double* gen_array(int n) {
	double* array = (double*) malloc(n*sizeof(double));
	for(int i=0; i<n; i++)
		array[i] = drand48();
	return array;
}

double dotp_naive(double* x, double* y) {
	double global_sum = 0.0;
	#pragma omp parallel
	{
		#pragma omp for
		for(int i=0; i<ARRAY_SIZE; i++)
			#pragma omp critical
				global_sum += x[i] * y[i];
	}
	return global_sum;
}

// EDIT THIS FUNCTION PART 1
double dotp_manual_optimized(double* x, double* y) {
     double global_sum = 0.0;
	#pragma omp parallel
	{
		#pragma omp for
		for(int i=0; i<ARRAY_SIZE; i++)
			#pragma omp critical
				global_sum += x[i] * y[i];
	}
	return global_sum;
}

// EDIT THIS FUNCTION PART 2
double dotp_reduction_optimized(double* x, double* y) {
     double global_sum = 0.0;
	#pragma omp parallel
	{
		#pragma omp for
		for(int i=0; i<ARRAY_SIZE; i++)
			#pragma omp critical
				global_sum += x[i] * y[i];
	}
	return global_sum;
}

int main() {
	// Generate input vectors
	double *x = gen_array(ARRAY_SIZE);
	double *y = gen_array(ARRAY_SIZE);
	double serial_result = 0.0;
	double result;

	// calculate result serially
	for(int i=0; i<ARRAY_SIZE; i++)
		serial_result += x[i] * y[i];

	// Test framework that sweeps the number of threads and times each ru
	double start_time, run_time;
	int num_threads = omp_get_max_threads();
	for(int i=1; i<=num_threads; i++) {
		omp_set_num_threads(i);
		start_time = omp_get_wtime();
		for(int j=0; j<REPEAT; j++)
			result = dotp_manual_optimized(x,y);
		run_time = omp_get_wtime() - start_time;
  		printf("Manual Optimized: %d thread(s) took %f seconds\n",i,run_time);

		// verify result is correct (within some threshold)
		if (fabs(serial_result - result) > 0.001) {
			printf("Incorrect result!\n");
			return -1;
		}
	}

  for(int i=1; i<=num_threads; i++) {
    omp_set_num_threads(i);
    start_time = omp_get_wtime();
    for(int j=0; j<REPEAT; j++)
      result = dotp_reduction_optimized(x,y);
    run_time = omp_get_wtime() - start_time;
      printf("Reduction Optimized: %d thread(s) took %f seconds\n",i,run_time);

    // verify result is correct (within some threshold)
    if (fabs(serial_result - result) > 0.001) {
      printf("Incorrect result!\n");
      return -1;
    }
  }

  // Only run this once because it's too slow..
	for(int i=1; i<=1; i++) {
		omp_set_num_threads(i);
		start_time = omp_get_wtime();
		for(int j=0; j<REPEAT; j++)
			result = dotp_naive(x,y);
		run_time = omp_get_wtime() - start_time;
  	printf("Naive: %d thread(s) took %f seconds\n",i,run_time);
	}
  return 0;
}
