/*********************
**  Color Map generator
** Skeleton by Justin Yokota
**********************/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>
#include "ColorMapInput.h"


/**************
**This function reads in a file name colorfile.
**It then uses the information in colorfile to create a color array, with each color represented by an int[3].
***************/
int** FileToColorMap(char* colorfile, int* colorcount)
{
	//YOUR CODE HERE
	FILE *ptr = fopen(colorfile, "r");
	if(ptr == NULL) return NULL;
	fscanf(ptr, "%d", colorcount);

	int **res;
	res = (int**)malloc((*colorcount)*sizeof(int*));
	for(int i=0; i<(*colorcount); i++){
		res[i] = (int*)malloc(3*sizeof(int));
	}
	
	for(int i=0; i<(*colorcount); i++){
		fscanf(ptr, "%d %d %d", &res[i][0], &res[i][1], &res[i][2]);
	}
	fclose(ptr);

	return res;
}




