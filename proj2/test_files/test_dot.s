.import ../dot.s
.import ../utils.s

# Set vector values for testing
.data
vector0: .word 4 5 6
vector1: .word 1 1 1


.text
# main function for testing
main:
    # Load vector addresses into registers
    la s0 vector0
    la s1 vector1

    # Set vector attributes
	mv a0 s0
	mv a1 s1
	addi a2 x0 3
	addi a3 x0 1
	addi a4 x0 1

    # Call dot function
    jal ra dot


    # Print integer result
	mv a1 a0
	jal print_int


    # Print newline
	li a1 '\n'
	jal print_char


    # Exit
    jal exit
