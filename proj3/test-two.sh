#!/bin/bash

./cpu-twostage-sanity.sh
python3 binary_to_hex.py twostage-tests/circ_files/reference_output/CPU-addi.out
printf "\n"
python3 binary_to_hex.py twostage-tests/circ_files/output/CPU-addi.out
java -jar logisim-evolution.jar
