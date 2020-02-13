#!/usr/bin/env python

import os
import os.path
import tempfile
import subprocess
import time
import signal
import re
import sys
import shutil

file_locations = os.path.expanduser(os.getcwd())
logisim_location = os.path.join(os.getcwd(),"../../logisim-evolution.jar")

class TestCase():
  """
      Runs specified circuit file and compares output against the provided reference trace file.
  """

  def __init__(self, circfile, tracefile, register_doc):
    self.circfile  = circfile
    self.tracefile = tracefile
    self.register_doc = register_doc

  def __call__(self, filename):
    output = tempfile.TemporaryFile(mode='r+')
    try:
      stdinf = open('/dev/null')
    except Exception as e:
      try:
        stdinf = open('nul')
      except Exception as e:
         print("Could not open nul or /dev/null. Program will most likely error now.")
    proc = subprocess.Popen(["java","-jar",logisim_location,"-tty","table",self.circfile], stdin=stdinf, stdout=subprocess.PIPE)
    try:
      reference = open(self.tracefile)
      passed = compare_unbounded(proc.stdout,reference, filename)
    finally:
      try: 
        os.kill(proc.pid,signal.SIGTERM)
      except Exception as e: 
        pass
    if passed:
      return (True, "Matched expected output")
    else:
      return (False, "Did not match expected output")

def compare_unbounded(student_out, reference_out, filename):
  passed = True
  student_output_array = []
  while True:
    line1 = student_out.readline().rstrip().decode("utf-8", "namereplace")
    line2 = reference_out.readline().rstrip()
    if line2 == '':
      break
    student_output_array.append(line1)
    m = re.match(line2, line1)
    if m == None or m.start() != 0 or m.end() != len(line2):
      passed = False
  with open(filename, "w") as student_output:
    for line in student_output_array:
      student_output.write(line + '\n')
  return passed


def run_tests(tests):
  print("Testing files...")
  tests_passed = 0
  tests_failed = 0

  for description,filename,test in tests:
    test_passed, reason = test(filename)
    if test_passed:
      print("\tPASSED test: %s" % description)
      tests_passed += 1
    else:
      print("\tFAILED test: %s (%s)" % (description, reason))
      tests_failed += 1
  
  print("Passed %d/%d tests" % (tests_passed, (tests_passed + tests_failed)))

tests = [
  ("ALU add test", "student_output/alu-add-student.out",TestCase(os.path.join(file_locations,'alu_tests/alu-add.circ'), os.path.join
(file_locations,'reference_output/alu-add-ref.out'), "")),
  ("ALU mult/mulhu test", "student_output/alu-mult-student.out", TestCase(os.path.join(file_locations,'alu_tests/alu-mult.circ'), os.path.join(file_locations,'reference_output/alu-mult-ref.out'), "")),
("ALU mulh test (extra credit)", "student_output/alu-mulh-student.out", TestCase(os.path.join(file_locations,'alu_tests/alu-mulh.circ'), os.path.join(file_locations,'reference_output/alu-mulh-ref.out'), "")),
  ("ALU div and rem test", "student_output/alu-div-rem-student.out", TestCase(os.path.join(file_locations,'alu_tests/alu-div-rem.circ'), os.path.join(file_locations,'reference_output/alu-div-rem-ref.out'), "")),
  ("ALU logic test", "student_output/alu-logic-student.out", TestCase(os.path.join(file_locations,'alu_tests/alu-logic.circ'), os.path.join(file_locations,'reference_output/alu-logic-ref.out'), "")),
  ("ALU shift test", "student_output/alu-shift-student.out", TestCase(os.path.join(file_locations,'alu_tests/alu-shift.circ'), os.path.join(file_locations,'reference_output/alu-shift-ref.out'), "")),
  ("ALU select, sub, BSel test", "student_output/alu-set-sub-bsel-student.out", TestCase(os.path.join(file_locations,'alu_tests/alu-set-sub-bsel.circ'), os.path.join(file_locations,'reference_output/alu-set-sub-bsel-ref.out'), "")),
("ALU comprehensive test", "student_output/alu-comprehensive-student.out", TestCase(os.path.join(file_locations,'alu_tests/alu-comprehensive.circ'), os.path.join(file_locations,'reference_output/alu-comprehensive-ref.out'), ""))

]

if __name__ == '__main__':
  run_tests(tests)
