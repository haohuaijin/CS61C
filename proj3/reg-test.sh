#!/bin/bash

# Just run this file and you can test your circ files!
# Make sure your files are in the directory above this one though!
# Credits to William Huang

cp regfile.circ part1-tests/reg-tests/regfile_tests
cd part1-tests/reg-tests
rm -rf student_output
mkdir student_output
chmod +x reg-test.py
./reg-test.py
cd ../..
