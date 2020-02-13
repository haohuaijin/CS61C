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
 ("RegFile insert test", "student_output/regfile-insert-student.out", TestCase(os.path.join(file_locations,'regfile_tests/regfile-insert.circ'), os.path.join(file_locations,'reference_output/regfile-insert-ref.out'), "")), 
  ("RegFile zero test", "student_output/regfile-zero-student.out", TestCase(os.path.join(file_locations,'regfile_tests/regfile-zero.circ'), os.path.join(file_locations,'reference_output/regfile-zero-ref.out'), "")),
  ("RegFile x0 test", "student_output/regfile-x0-student.out", TestCase(os.path.join(file_locations,'regfile_tests/regfile-x0.circ'), os.path.join(file_locations,'reference_output/regfile-x0-ref.out'), "")),
  ("RegFile all registers test", "student_output/regfile-allregs-student.out", TestCase(os.path.join(file_locations,'regfile_tests/regfile-allregs.circ'), os.path.join(file_locations,'reference_output/regfile-allregs-ref.out'), ""))

]

if __name__ == '__main__':
  run_tests(tests)
