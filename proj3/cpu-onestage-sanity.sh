#!/bin/bash

cp mem.circ onestage-tests/circ_files
cp alu.circ onestage-tests/circ_files
cp regfile.circ onestage-tests/circ_files
cp cpu.circ onestage-tests/circ_files
cd onestage-tests/circ_files
chmod +x sanity_test.py
./sanity_test.py
cd ../..
