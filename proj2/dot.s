.globl dot

.text
# =======================================================
# FUNCTION: Dot product of 2 int vectors
# Arguments:
#   a0 is the pointer to the start of v0
#   a1 is the pointer to the start of v1
#   a2 is the length of the vectors
#   a3 is the stride of v0
#   a4 is the stride of v1
# Returns:
#   a0 is the dot product of v0 and v1
# =======================================================
dot:

    # Prologue
	addi sp sp -12
	sw ra 0(sp)
	sw s0 4(sp)
	sw s1 8(sp)

	add s0 a0 x0 # s0 is the pointer of v0
	add s1 a1 x0 # s1 is the pointer 0f v1
	add t0 a2 x0 # t0 is length
	add t1 x0 x0 # t1 is the count
	add t2 x0 x0 #the result

	slli a3 a3 2
	slli a4 a4 2

loop_start:
	lw t3 0(s0)
	lw t4 0(s1)
	
	mul t3 t3 t4
	add t2 t2 t3 # the result of the mul v0[]*v1[]

	add s0 s0 a3
	add s1 s1 a4
	addi t1 t1 1

	bne t0 t1 loop_start

loop_end:

	mv a0 t2

    # Epilogue
	lw s1 8(sp)
    lw s0 4(sp)
	lw ra 0(sp)
	addi sp sp 12
    ret
