#!/usr/bin/python

import sys
import argparse

parser = argparse.ArgumentParser(description="Manually sort a list depending on human subjective input.")
parser.add_argument('file', metavar='FILE', help="line separated file to read list from")
parser.parse_args()

values = []
valid_choices = [1,2,3,4,5]
choice = None

with open(sys.argv[1], "r") as file:
  for line in file:
    print line.rstrip()
    
    while choice not in valid_choices:
      try:
        choice = int(raw_input("Enter grade [1-5] (1 is highest) : "))
        values.append([line.rstrip(), choice]) 
      except ValueError:
        pass
      
    choice = None

values = sorted(values, key=lambda values: values[1])

for value in values:
  print value[0]

