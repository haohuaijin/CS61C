#!/bin/bash

cp mem.circ twostage-tests/circ_files
cp alu.circ twostage-tests/circ_files
cp regfile.circ twostage-tests/circ_files
cp cpu.circ twostage-tests/circ_files
cd twostage-tests/circ_files
chmod +x sanity_test.py
./sanity_test.py
cd ../..
