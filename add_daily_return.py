#!/usr/bin/env python3
import sys
import csv

def process_line(line):
    if not line.strip():
        return None
    
    # Handle header
    if line.startswith('Date'):
        return line.strip() + ',daily_return\n'
    
    try:
        # Parse CSV line
        reader = csv.reader([line])
        row = next(reader)
        
        # Calculate daily return
        close = float(row[4])
        open_price = float(row[1])
        daily_return = ((close - open_price) / open_price) * 100
        
        # Format daily return to 2 decimal places
        return f"{line.strip()},{daily_return:.2f}\n"
    except Exception as e:
        print(f"ERROR processing line: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    for line in sys.stdin:
        result = process_line(line)
        if result:
            print(result, end='') 