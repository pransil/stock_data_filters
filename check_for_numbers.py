#!/usr/bin/env python3
# check_open_hi_lo_close_adj_close.py are all numbers   

# format: Date, Open, High, Low, Close, Adj Close, Volume

import sys
import csv

def convert_and_validate(row):
    converted = []
    for item in row:
        try:
            num = int(item)
        except ValueError:
            try:
                num = float(item)
            except ValueError:
                print(f"Error: '{item}' is not a number.")
                continue
        converted.append(num)
    return converted


def process_line(line):
    if not line.strip():
        return None
    
    # Skip header
    if line.startswith('Date'):
        return line
    
    new_line = []
    try:
        # Parse CSV line
        reader = csv.reader([line])
        row = next(reader)
       # remove the first item (it should be the date)
        new_line.append(row[0])
        row2 = row[1:]
        # check each item in row2 is a number string that can be converted to a float 
        for item in row2:
            try:
                number =float(item)
                #print(f"number: {number}")
                # round the item to 2 decimal places
                number = round(number, 2)
                #print(f"rounded number: {number}")

                new_line.append(f"{number}")
            except ValueError:
                print(f"Invalid number: {item}", file=sys.stderr)
                return None
        # assemble a new csv line from new_line and return it as a filtered line with a newline character at the end    
        return ','.join(new_line) + '\n'
    except Exception as e:
        print(f"Error processing line: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    for line in sys.stdin:
        result = process_line(line)
        if result:
            print(result, end='') 
