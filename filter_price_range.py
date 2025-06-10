#!/usr/bin/env python3
import sys
import csv

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
        
        # Calculate price range
        high = float(row[2])
        low = float(row[3])
        price_range = high - low
        
        if price_range >= 1.0:
            return line
        return None
    except Exception as e:
        print(f"Error processing line: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    for line in sys.stdin:
        result = process_line(line)
        if result:
            print(result, end='') 