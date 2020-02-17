.import read_matrix.s
.import write_matrix.s
.import matmul.s
.import dot.s
.import relu.s
.import argmax.s
.import utils.s

.globl main

.text
main:
    # =====================================
    # COMMAND LINE ARGUMENTS
    # =====================================
    # Args:
    #   a0: int argc
    #   a1: char** argv
    #
    # Usage:
    #   main.s <M0_PATH> <M1_PATH> <INPUT_PATH> <OUTPUT_PATH>

    # Exit if incorrect number of command line args
    mv s0 a1 # s0 is the argv
    addi t0 x0 5
    bne t0 a0 error

	# =====================================
    # LOAD MATRICES
    # =====================================


# Load pretrained m0
    
    lw s1 8(s0)
    #malloc the rows
    addi a0 x0 4
    jal ra malloc
    mv a1 a0
    #malloc the columns
    addi a0 x0 4
    jal ra malloc
    mv a2 a0
    
    mv a0 s1 
    jal ra read_matrix
    
    mv s1 a0 # the pointer
    lw s2 0(a1) # the row
    lw s3 0(a2) # the columns


# # Load pretrained m1

#     lw s4 8(s0)
#     #malloc the rows
#     addi a0 x0 4
#     jal ra malloc
#     mv a1 a0
#     #malloc the columns
#     addi a0 x0 4
#     jal ra malloc
#     mv a2 a0

#     mv a0 s4 
#     jal ra read_matrix
    
#     mv s4 a0 # the pointer
#     lw s5 0(a1) # the row
#     lw s6 0(a2) # the columns


# # Load input matrix

#     lw s7 12(s0)
#     #malloc the rows
#     addi a0 x0 4
#     jal ra malloc
#     mv a1 a0
#     #malloc the columns
#     addi a0 x0 4
#     jal ra malloc
#     mv a2 a0

#     mv a0 s7 
#     jal ra read_matrix
    
#     mv s7 a0 # the pointer
#     lw s8 0(a1) # the row
#     lw s9 0(a2) # the columns
    


#     # =====================================
#     # RUN LAYERS
#     # =====================================
#     # 1. LINEAR LAYER:    m0 * input
#     # 2. NONLINEAR LAYER: ReLU(m0 * input)
#     # 3. LINEAR LAYER:    m1 * ReLU(m0 * input)

# # first matmul
#     mul a0 s2 s9 
#     slli a0 a0 2
#     jal ra malloc

#     mv a6 a0 # the result
#     mv a0 s1
#     mv a1 s2
#     mv a2 s3
#     mv a3 s7
#     mv a4 s8
#     mv a5 s9
#     jal ra matmul

#     # save the result
#     mv s1 a6
#     mv s2 a1 # rows
#     mv s3 a5 # columns


# # second relu
#     mv a0 s1
#     mul a1 s2 s3
#     jal ra relu


# # third matmul
#     mul a0 s5 s3
#     slli a0 a0 2
#     jal ra malloc

#     mv a6 a0
#     mv a0 s4
#     mv a1 s5
#     mv a2 s6
#     mv a3 s1
#     mv a4 s2
#     mv a5 s3
#     jal ra matmul

#     # save the result
#     mv s1 a6
#     mv s2 a1 # rows
#     mv s3 a5 # columns



#     # =====================================
#     # WRITE OUTPUT
#     # =====================================
#     # Write output matrix
#     lw a0 16(s0) # Load pointer to output filename
#     mv a1 s1 # pointer
#     mv a2 s2 # rows
#     mv a3 s3 # columns
#     jal ra write_matrix



#     # =====================================
#     # CALCULATE CLASSIFICATION/LABEL
#     # =====================================
#     # Call argmax
#     mv a0 s1
#     mul a1 s2 s3
#     jal ra argmax


#     # Print classification
#     mv a1 a0
#     jal ra print_int


#     # Print newline afterwards for clarity
#     li a1 '\n'
#     jal print_char

    jal exit


error:
    li a1 1
    jal exit2