#!/usr/bin/env python3

from __future__ import print_function
import os
import os.path
import tempfile
import subprocess
import time
import signal
import re
import sys
import shutil

create = 0
log = 0

file_locations = os.path.expanduser(os.getcwd())
logisim_location = os.path.join(os.getcwd(),"../../logisim-evolution.jar")
if log:
  new = open('new.out', 'w')
  logfile = open('TEST_LOG','w')


def student_reference_match_unbounded(student_out, reference_out):
  while True:
    line1 = student_out.readline()
    line2 = reference_out.readline()
    if line2 == '':
      break
    if line1 != line2:
      return False
  return True

def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
                os.makedirs(dir)      

class TestCase(object):
  def __init__(self, circfile, outfile, tracefile, points):
    self.circfile  = circfile
    self.outfile = outfile
    self.tracefile = tracefile
    self.points = points

class AbsoluteTestCase(TestCase):
  """
  All-or-nothing test case.
  """
  def __call__(self):
    output = tempfile.TemporaryFile(mode='r+')
    try:
      stdinf = open('/dev/null')
    except Exception as e:
      try:
        stdinf = open('nul')
      except Exception as e:
         print("The no nul directories. Program will most likely error now.")
    proc = subprocess.Popen(["java","-jar",logisim_location,"-tty","table",self.circfile], stdin=stdinf, stdout=subprocess.PIPE)
    try:
      assure_path_exists(self.outfile)
      outfile = open(self.outfile, "wb")
      student_out = proc.stdout.read()
      outfile.write(student_out)
      outfile.close()
      assure_path_exists(self.outfile)
      outfile = open(self.outfile, "r")
      reference = open(self.tracefile)
      passed = student_reference_match_unbounded(outfile, reference)
    finally:
      try:
        os.kill(proc.pid,signal.SIGTERM)
      except Exception as e:
        pass
    if passed:
      return (self.points,"Matched expected output")
    else:
      return (0,"Did not match expected output")



def test_submission(name,outfile,tests):
  # actual submission testing code
  print ("Testing your tests (two-stage processor)...")
  total_points = 0
  total_points_received = 0
  tests_passed = 0
  tests_partially_passed = 0
  tests_failed = 0
  test_results = []
  for description,test,points_received,reason in ((description,test) + test() for description,test in tests): # gross
    points = test.points
    assert points_received <= points
    if points_received == points:
      print ("\t%s PASSED test: %s" % (name, description))
      if log:
        print ("\t%s PASSED test: %s" % (name, description), file=logfile)

      total_points += points
      total_points_received += points
      tests_passed += 1
      test_results.append("\tPassed test \"%s\" worth %d points." % (description,points))
    elif points_received > 0:
      print ("\t%s PARTIALLY PASSED test: %s" % (name,description))
      if log:
        print ("\t%s PARTIALLY PASSED test: %s" % (name,description), file=logfile)
      total_points += points
      total_points_received += points_received
      tests_partially_passed += 1
      test_results.append("\tPartially passed test \"%s\" worth %d points (received %d)" % (description, points, points_received))
    else:
      print ("\t%s FAILED test: %s" % (name, description))
      if log:
        print ("\t%s FAILED test: %s" % (name, description), file=logfile)
      total_points += points
      tests_failed += 1
      test_results.append("\tFailed test \"%s\" worth %d points. Reason: %s" % (description, points, reason))
  
  print ("\tScore for %s: %d/%d (%d/%d tests passed, %d partially)" %\
    (name, total_points_received, total_points, tests_passed, 
     tests_passed + tests_failed + tests_partially_passed, tests_partially_passed))
  print ("%s: %d/%d (%d/%d tests passed, %d partially)" %\
    (name, total_points_received, total_points, tests_passed,
     tests_passed + tests_failed + tests_partially_passed, tests_partially_passed), file=outfile)
  if log:
    print ("\n\n%s: %d/%d (%d/%d tests passed, %d partially)" %\
    (name, total_points_received, total_points, tests_passed,
     tests_passed + tests_failed + tests_partially_passed, tests_partially_passed), file=logfile)
  for line in test_results:
    print (line, file=outfile)
    if log:
      print ( line, file=logfile)
  
  return points_received



def main(tests):
  test_submission('you',sys.stdout,tests)
    
