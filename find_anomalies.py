# find anomalies in the data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load the data
#data = pd.read_csv('data.csv')

# find anomalies
# format: Date, Open, High, Low, Close, Adj Close, Volume

# Read file, one line at a time
with open('kaggle_stock_data/stocks/tesla.csv', 'r') as file:
    # marker for first line
    first = True
    count = 0
    anomalies = 0
    for line in file:
        print(line)
        # split the line into a list
        line = line.split(',')
        # if first line, set line_len to the length of the line
        if first:
            line_len = len(line)
            first = False
        # if the line is not the same length as the first line, print the line
        if len(line) != line_len:
            print(f"Line {count} is ", len(line), "items, should have ", line_len, " items.")
            print(line)
            anomalies += 1
        count += 1
        if count >= 100:
            break
    print(f"Total anomalies: {anomalies} out of {count} lines.")

