#!/usr/bin/env python

import autograder_base
import os.path

from autograder_base import file_locations, AbsoluteTestCase, main

tests = [
("CPU addi test",AbsoluteTestCase(os.path.join(file_locations,'CPU-addi.circ'), os.path.join(file_locations,'output/CPU-addi.out'), os.path.join(file_locations,'reference_output/CPU-addi.out'),1)),
  ("CPU add/lui/sll test",AbsoluteTestCase(os.path.join(file_locations,'CPU-add_lui_sll.circ'), os.path.join(file_locations,'output/CPU-add_lui_sll.out'), os.path.join(file_locations,'reference_output/CPU-add_lui_sll.out'),1)),
  ("CPU memory test",AbsoluteTestCase(os.path.join(file_locations,'CPU-mem.circ'), os.path.join(file_locations,'output/CPU-mem.out'), os.path.join(file_locations,'reference_output/CPU-mem.out'),1)),
  ("CPU branch test",AbsoluteTestCase(os.path.join(file_locations,'CPU-branches.circ'), os.path.join(file_locations,'output/CPU-branches.out'), os.path.join(file_locations,'reference_output/CPU-branches.out'),1)),
  ("CPU jump test",AbsoluteTestCase(os.path.join(file_locations,'CPU-jump.circ'), os.path.join(file_locations,'output/CPU-jump.out'), os.path.join(file_locations,'reference_output/CPU-jump.out'),1)),
  ("CPU br_jalr test",AbsoluteTestCase(os.path.join(file_locations,'CPU-br_jalr.circ'), os.path.join(file_locations,'output/CPU-br_jalr.out'), os.path.join(file_locations,'reference_output/CPU-br_jalr.out'),1))
]


if __name__ == '__main__':
  main(tests)
