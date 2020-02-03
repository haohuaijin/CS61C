/*********************
**  Complex Numbers
**  This file contains a few functions that will be useful when performing computations with complex numbers
**  It is advised that you work on this part first.
**********************/



#include <stdio.h>
#include <stdlib.h>
typedef struct ComplexNumber ComplexNumber;

//Returns a pointer to a new Complex Number with the given real and imaginary components
extern ComplexNumber* newComplexNumber(double real_component, double imaginary_component);

//Returns a pointer to a new Complex Number equal to a*b
extern ComplexNumber* ComplexProduct(ComplexNumber* a, ComplexNumber* b);

//Returns a pointer to a new Complex Number equal to a+b
extern ComplexNumber* ComplexSum(ComplexNumber* a, ComplexNumber* b);

//Returns the absolute value of Complex Number a
extern double ComplexAbs(ComplexNumber* a);

//Frees the complex number
extern void freeComplexNumber(ComplexNumber* a);

extern int test_complex_number();

//Gets the real component of the complex number
extern double Re(ComplexNumber* a);
//Gets the imaginary component of the complex number
extern double Im(ComplexNumber* a);
