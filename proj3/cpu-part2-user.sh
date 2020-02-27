#!/bin/bash

cp mem.circ my_tests/circ_files
cp alu.circ my_tests/circ_files
cp regfile.circ my_tests/circ_files
cp cpu.circ my_tests/circ_files
cd my_tests/circ_files
chmod +x modular_test.py
./modular_test.py
cd ../..
