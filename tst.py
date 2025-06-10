#!/usr/bin/env python3
import sys
import csv

def process_line(line, prev_close):
      return line, prev_close

count = 0
for line in sys.stdin:
    if count == 0:
        print(line.strip())
        count += 1
        continue
    # split the line into a list
    line = line.strip()
    line = line.split(',')
    if count == 1:
        prev_close = float(line[1])
   
    line, prev_close = process_line(line, prev_close)
    print(line) 
    #print(f"line[3]: {line[3]}")

