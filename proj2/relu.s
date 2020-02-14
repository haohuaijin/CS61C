.globl relu

.text
# ==============================================================================
# FUNCTION: Performs an inplace element-wise ReLU on an array of ints
# Arguments:
# 	a0 is the pointer to the array
#	a1 is the # of elements in the array
# Returns:
#	None
# ==============================================================================
relu:
    # Prologue
	addi sp  sp  -12
	lw ra  0(sp)
	lw s0  4(sp)
	lw s1  8(sp)

	add s0  a0  x0 # s0 save a0
	add s1  a1  x0 # s1 save a1
	add t0  x0  x0 # count the array number
		
loop_start:
	lw t1  0(s0)
	bgez t1  loop_continue
	sw x0  0(s0)

loop_continue:
	addi s0  s0  4
	addi t0  t0  1
	beq s1  t0  loop_end
	j loop_start

loop_end:
    # Epilogue
	sw s1  8(sp)
	sw s0  4(sp)
	sw ra  0(sp)
    addi sp  sp  12
	ret




