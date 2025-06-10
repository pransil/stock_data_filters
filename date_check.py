#!/usr/bin/env python3
# date_check.py

# check if the first item in the line is a valid date
# format: Date, Open, High, Low, Close, Adj Close, Volume

import sys
import csv
from datetime import datetime

def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def process_line(line):
    if not line.strip():
        return None
    
    # Skip header
    if line.startswith('Date'):
        return line
    
    try:
        # Parse CSV line
        reader = csv.reader([line])
        row = next(reader)

        # check if the first item in the line is a valid date
        date = row[0]
        date_valid = is_valid_date(date)
        if not date_valid:
            print(f"Invalid date: {date}", file=sys.stderr)
            #return None

        
        return line
    except Exception as e:
        print(f"Error processing line: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    for line in sys.stdin:
        result = process_line(line)
        if result:
            print(result, end='') 
