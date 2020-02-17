.globl write_matrix

.text
# ==============================================================================
# FUNCTION: Writes a matrix of integers into a binary file
#   If any file operation fails or doesn't write the proper number of bytes,
#   exit the program with exit code 1.
# FILE FORMAT:
#   The first 8 bytes of the file will be two 4 byte ints representing the
#   numbers of rows and columns respectively. Every 4 bytes thereafter is an
#   element of the matrix in row-major order.
# Arguments:
#   a0 is the pointer to string representing the filename
#   a1 is the pointer to the start of the matrix in memory
#   a2 is the number of rows in the matrix
#   a3 is the number of columns in the matrix
# Returns:
#   None
# ==============================================================================
write_matrix:

    # Prologue
    addi sp sp -20
    sw ra 0(sp)
    sw s0 4(sp)
    sw s1 8(sp)
    sw s2 12(sp)
    sw s3 16(sp)

    mv s0 a0 # the file path
    mv s1 a1 # the matrix
    mv s2 a2 # the rows
    mv s3 a3 # the columns

    mv a1 s0
    addi a2 x0 1
    jal ra fopen
    addi t0 x0 -1
    beq t0 a0 eof_or_error

    mv s0 a0 # save the file descriptor

    # write rows

    addi a0 x0 4
    jal ra malloc
    sw s2 0(a0)    
    mv a1 s0
    mv a2 a0
    addi a3 x0 1
    addi a4 x0 4
    jal ra fwrite
    bne a0 a3 eof_or_error

    # write colums
    addi a0 x0 4
    jal ra malloc
    sw s3 0(a0)
    mv a1 s0
    mv a2 a0
    addi a3 x0 1
    addi a4 x0 4
    jal ra fwrite
    bne a0 a3 eof_or_error


    mv a1 s0
    mv a2 s1
    mul t0 s2 s3 #the number of item
    mv a3 t0
    addi t0 x0 4
    mv a4 t0
    jal ra fwrite
    bne a0 a3 eof_or_error

    jal ra fclose
    bne a0 x0 eof_or_error


    # Epilogue
    lw s3 16(sp)
    lw s2 12(sp)
    lw s1 8(sp)
    lw s0 4(sp)
    lw ra 0(sp)
    addi sp sp 20
    ret

eof_or_error:
    li a1 1
    jal exit2
    