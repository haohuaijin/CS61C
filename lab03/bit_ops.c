#include <stdio.h>
#include "bit_ops.h"

// Return the nth bit of x.
// Assume 0 <= n <= 31
unsigned get_bit(unsigned x,
                 unsigned n) {
    // YOUR CODE HERE
    // Returning -1 is a placeholder (it makes
    // no sense, because get_bit only returns 
    // 0 or 1)
	
	//return	((x>>n)<<31)>>(31);
	return x>>n<<31>>31;
	
	//return -1;
}
// Set the nth bit of the value of x to v.
// Assume 0 <= n <= 31, and v is 0 or 1
void set_bit(unsigned * x,
             unsigned n,
             unsigned v) {
    // YOUR CODE HERE
	unsigned a = 1;
	unsigned b = 0;
	b = ~b; 
	b = b<<(n+1);

	v = ~v;
	v = v << n;
	v = ~v;
	v = v|b;

	a = a << n;

	(*x) = (*x)|a;
	(*x) = (*x)&v;
}
// Flip the nth bit of the value of x.
// Assume 0 <= n <= 31
void flip_bit(unsigned * x,
              unsigned n) {
    // YOUR CODE HERE
	unsigned a = get_bit(*x, n);
	a = ~a;
	a = a<<31>>31;
	set_bit(x, n, a);
}






