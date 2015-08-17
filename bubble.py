#!/usr/bin/python

import signal
import sys
import itertools
import os
import argparse

parser = argparse.ArgumentParser(description="Manually bubble sort a list depending on human subjective input.")
parser.add_argument('file', metavar='INPUT', help="line separated file to read list from")
parser.add_argument('file', metavar='OUTPUT', help="line separated file to write list to")
parser.parse_args()

try:
  input = open(sys.argv[1], "r")
except Exception:
  print sys.argv[1]+" file not found"
  sys.exit(1)

try:
  output = open(sys.argv[2], "w")
except Exception:
  print sys.argv[2]+" file error"
  sys.exit(1)


def signal_handler(signal, frame):
  print " exiting... writing result to "+sys.argv[2]
#  print '%s' % '\n'.join(map(str, values))
  output.write('\n'.join(map(str, values))) 
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

valid_choices = [1,2]
choice = None

values = []
for line in input:
  values.append(line.rstrip())

pointer = 0
length = len(values)

while True:
  os.system("clear")
  if pointer == length-1:
    pointer = 0
  while choice not in valid_choices:
    print "(1) "+values[pointer]
    print "(2) "+values[pointer+1]
    try:
      choice = int(raw_input("Enter your choice [1-2] : "))
    except ValueError:
      pass 
  if choice == 2:
    v = values[pointer+1]
    values[pointer+1] = values[pointer]
    values[pointer] = v
  choice = None
  pointer+=1

signal.pause()
