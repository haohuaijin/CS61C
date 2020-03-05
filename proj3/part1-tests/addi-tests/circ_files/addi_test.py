#!/usr/bin/env python

import autograder_base
import os.path
import sys

from autograder_base import file_locations, AbsoluteTestCase, main
s_or_p = sys.argv[1]

tests = [
("CPU addi test",AbsoluteTestCase(os.path.join(file_locations,'CPU-addi.circ'), os.path.join(file_locations,'student_output/CPU-addi-' + s_or_p + '.out'), os.path.join(file_locations,'reference_output/CPU-addi-' + s_or_p + '.out'),1)),
]


if __name__ == '__main__':
  main(tests)
