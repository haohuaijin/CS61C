#!/usr/bin/env python3

import autograder_base
import os.path
import os

from autograder_base import file_locations, AbsoluteTestCase, main

testTag = "CPU-"
testEnd = ".circ"

tests = []

for filename in os.listdir(os.getcwd()):
    if filename.startswith(testTag) and filename.endswith(testEnd):
        testname = (filename[len(testTag):])[:-len(testEnd)]
        tests.append(("CPU " + testname + " test",AbsoluteTestCase(os.path.join(file_locations,'CPU-' + testname + '.circ'), os.path.join(file_locations,'output/CPU-' + testname + '.out'), os.path.join(file_locations,'reference_output/CPU-' + testname + '.out'),1)))

if __name__ == '__main__':
    if tests:
        main(tests)
    else:
        print("Please make some tests before you run this file!")
