#!/bin/bash

./cpu-twostage-sanity.sh
printf "\n"
python3 binary_to_hex.py twostage-tests/circ_files/output/CPU-add_lui_sll.out
printf "\n"
python3 binary_to_hex.py twostage-tests/circ_files/reference_output/CPU-add_lui_sll.out
java -jar logisim-evolution.jar
