#!/usr/bin/env python3
# convert_to_deltas.py  -  Subtract the previous day's close values from Open, High, Low, Close

# format: Date, Open, High, Low, Close, Adj Close, Volume

import sys
import csv

def ten_day_volume_exp_average(volume, avg):
    return 0.1 * volume + 0.9 * avg

def list_to_csv_line(my_list):
    #print(f"my_list: {my_list}")
    line = ','.join(str(item) for item in my_list)
    #print(f"line: {line}")
    return line

def process_line(line, prev_close, prev_adj_close, prev_ten_day_volume_exp_average):    
    # Subtact prev_close from Open, High, Low, Close
    # return the new line as a string with a newline character at the end
    try:

       line[1] = round(float(line[1]) - float(prev_close), 2)

       line[2] = round(float(line[2]) - float(prev_close), 2)
       line[3] = round(float(line[3]) - float(prev_close), 2)
       line[4] = round(float(line[4]) - float(prev_close), 2)
       line[5] = round(float(line[5]) - float(prev_adj_close), 2)

       new_avg = ten_day_volume_exp_average(float(line[6]), prev_ten_day_volume_exp_average)
       #print(f"new_avg: {new_avg}")

       line[6] = round(float(line[6]) - prev_ten_day_volume_exp_average, 2)
       #print(f"Processing line: {line}")   
       new_line = list_to_csv_line(line)
       #print(f"Processing line: {line}")    
       #print(f"new_line: {new_line}")
       
       return new_line, new_avg
    except Exception as e:
        print(f"Error processing line: {e}", file=sys.stderr)
        return None, -1

if __name__ == "__main__":
    count = 0
    for line in sys.stdin:
        if count == 0:
            print(line.strip())
            count = 1
            continue
        # split the line into a list
        line = line.strip()
        line = line.split(',')
        if count == 1:
            prev_close = float(line[1])
            prev_adj_close = float(line[5])
            prev_ten_day_volume_exp_average = float(line[6])
  
        new_line, new_avg = process_line(line,prev_close, prev_adj_close, prev_ten_day_volume_exp_average)
        prev_close = float(line[1])
        prev_adj_close = float(line[5])
        prev_ten_day_volume_exp_average = float(line[6])
        print(new_line) 
        count += 1
    #print(f"line[3]: {line[3]}")


