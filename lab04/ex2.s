.data
source:
    .word   3
    .word   1
    .word   4
    .word   1
    .word   5
    .word   9
    .word   0
dest:
    .word   0
    .word   0
    .word   0
    .word   0
    .word   0
    .word   0
    .word   0
    .word   0
    .word   0
    .word   0

.text
main:
    addi t0, x0, 0
    la t1, source
    la t2, dest
loop:
    slli t3, t0, 2
    add t4, t1, t3
    lw t5, 0(t4)
    beq t5, x0, exit
    add t6, t2, t3
    sw t5, 0(t6)
    addi t0, t0, 1
    jal x0, loop
exit:
    addi a0, x0, 10
    add a1, x0, x0
    ecall # Terminate ecall