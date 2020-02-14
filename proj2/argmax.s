.globl argmax

.text
# =================================================================
# FUNCTION: Given a int vector, return the index of the largest
#	element. If there are multiple, return the one
#	with the smallest index.
# Arguments:
# 	a0 is the pointer to the start of the vector
#	a1 is the # of elements in the vector
# Returns:
#	a0 is the first index of the largest element
# =================================================================
argmax:

    # Prologue
	addi sp sp -12
	sw ra 0(sp)
	sw s0 4(sp)
	sw s1 8(sp)
	
	add s0 a0 x0
	add s1 a1 x0
	addi t0 x0 1
	
	# initial max to the first element of array
	lw t1 0(s0)
	addi s0 s0 4

loop_start:
	
	lw t2 0(s0)
	bge t1 t2 loop_continue
	mv t1 t2 # max is t2

loop_continue:
	
	addi s0 s0 4
	addi t0 t0 1
	beq t0 s1 loop_end
	j loop_start


loop_end:

    mv a0 t1

	# Epilogue
	lw s1 8(sp)
	lw s0 4(sp)
	lw ra 0(sp)
	addi sp sp 12
    ret
