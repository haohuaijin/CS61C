.globl matmul

.text
# =======================================================
# FUNCTION: Matrix Multiplication of 2 integer matrices
# 	d = matmul(m0, m1)
#   If the dimensions don't match, exit with exit code 2
# Arguments:
# 	a0 is the pointer to the start of m0
#	a1 is the # of rows (height) of m0
#	a2 is the # of columns (width) of m0
#	a3 is the pointer to the start of m1
# 	a4 is the # of rows (height) of m1
#	a5 is the # of columns (width) of m1
#	a6 is the pointer to the the start of d
# Returns:
#	None, sets d = matmul(m0, m1)
# =======================================================
matmul:

    # Error if mismatched dimensions
    bne a2 a4 mismatched_dimensions
    
    # Prologue
    addi sp sp -28
    sw ra 0(sp) 
    sw s0 4(sp) 
    sw s1 8(sp) 
    sw s2 12(sp) 
    sw s3 16(sp)
    sw s4 20(sp)
    sw s5 24(sp)

    add s0 a0 x0 # the pointer of m0
    add s1 a3 x0 # the pointer of m1
    add s2 a6 x0 # the pointer of the result
    add s4 a1 x0 # the rows of the m0
    add s5 a5 x0 # the colouns of the m1

    addi a3 x0 1 # the stride of m0 vector
    add a4 s5 x0 # the stride of m1 vector

    add a5 s0 x0 # use m0 pointer in loop
    add a6 s1 x0 # use m1 pointer in loop

    add s3 x0 x0 # use to end the out loop i

outer_loop_start:
    add t5 x0 x0 # use to the innner loop j

    add a0 a5 x0 # m0
    add a1 a6 x0 # m1

inner_loop_start:

    addi a3 x0 1 # the stride of m0 vector
    add a4 s5 x0 # the stride of m1 vector
    jal ra dot

    # find the index of result
    mul t6 s3 a2
    add t6 t6 t5
    slli t6 t6 2
    add t6 t6 s2

    sw a0 0(t6)

    # modified the address
    addi t5 t5 1

    add a0 a5 x0
    slli t6 t5 2
    add a1 a6 t6

    beq t5 s5 inner_loop_end
    j inner_loop_start

inner_loop_end:

    slli t6 a2 2 
    add a5 a5 t6

    addi s3 s3 1
    beq s3 s4 outer_loop_end
    j outer_loop_start

outer_loop_end:

    mv a6 s2
    mv a1 s4
    mv a5 s5

    # Epilogue
    lw s5 24(sp)
    lw s4 20(sp)
    lw s3 16(sp)
    lw s2 12(sp)
    lw s1 8(sp) 
    lw s0 4(sp)
    lw ra 0(sp) 
    addi sp sp 28
    ret

mismatched_dimensions:
    li a1 2
    jal exit2
