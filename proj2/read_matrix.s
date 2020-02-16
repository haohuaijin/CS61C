.globl read_matrix

.text
# ==============================================================================
# FUNCTION: Allocates memory and reads in a binary file as a matrix of integers
#   If any file operation fails or doesn't read the proper number of bytes,
#   exit the program with exit code 1.
# FILE FORMAT:
#   The first 8 bytes are two 4 byte ints representing the # of rows and columns
#   in the matrix. Every 4 bytes afterwards is an element of the matrix in
#   row-major order.
# Arguments:
#   a0 is the pointer to string representing the filename
#   a1 is a pointer to an integer, we will set it to the number of rows
#   a2 is a pointer to an integer, we will set it to the number of columns
# Returns:
#   a0 is the pointer to the matrix in memory
# ==============================================================================
read_matrix:

    # Prologue
	addi sp sp -16
    sw ra 0(sp)
    sw s0 4(sp)
    sw s1 8(sp)
    sw s2 12(sp)
    
    mv s0 a0
    mv s1 a1
    mv s2 a2

    # open file
    addi a1 s0 0
    addi a2 x0 0
    jal ra fopen
    #当打开文件失败时
    addi t0 x0 -1 
    beq a0 t0 eof_or_error

    mv s0 a0 # save the file descriptor

    # read the rows
    mv a1 s0
    mv a2 s1
    addi a3 x0 4
    jal ra fread 
    addi t0 x0 4
    bne a0 t0 eof_or_error
    lw t1 0(a2) # save rows to t1

    # read coloums
    mv a1 s0
    mv a2 s2
    addi a3 x0 4
    jal ra fread 
    addi t0 x0 4
    bne a0 t0 eof_or_error
    lw t2 0(a2) # save coloums to t2

    # read matrix
    mul a0 t1 t2
    slli a0 a0 2
    jal ra malloc
    beq a0 x0 eof_or_error # 如果未分配，报错

    mv a1 s0
    mv a2 a0
    mul a3 t1 t2
    slli a3 a3 2
    jal ra fread
    mul t0 t1 t2
    slli t0 t0 2
    bne t0 a0 eof_or_error

    mv a0 a2 
    mv a1 s1
    mv a2 s2

    # Epilogue
    lw s2 12(sp)
    lw s1 8(sp)
    lw s0 4(sp)
    lw ra 0(sp)
    addi sp sp 4
    ret

eof_or_error:
    li a1 1
    jal exit2
    