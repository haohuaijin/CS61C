#!/bin/bash

./cpu-twostage-sanity.sh
printf "\n"
python binary_to_hex.py twostage-tests/circ_files/output/CPU-jump.out
printf "\n"
python binary_to_hex.py twostage-tests/circ_files/reference_output/CPU-jump.out
java -jar logisim-evolution.jar