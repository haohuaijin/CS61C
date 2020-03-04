#!/bin/bash

./cpu-part1-pipelined.sh
cd part1-tests/addi-tests
python3 binary_to_hex.py circ_files/student_output/CPU-addi-pipelined.out
printf "\n"
python3 binary_to_hex.py circ_files/reference_output/CPU-addi-pipelined.out
cd ../..
java -jar logisim-evolution.jar