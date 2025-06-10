#!/bin/bash

# Check if input file is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_csv_file>"
    exit 1
fi

input_file="$1"
output_file="${input_file%.csv}.filtered.csv"

# Make sure the Python scripts are executable
chmod +x filter_volume.py
chmod +x filter_price_range.py
chmod +x add_daily_return.py

# Run the pipeline
cat "$input_file" | \
    ./date_check.py  | \
    ./check_for_numbers.py| \
    ./convert_to_deltas.py > "$output_file"
#    ./filter_volume.py | \
#    ./filter_price_range.py | \
#    ./add_daily_return.py \
    

echo "Processing complete. Output written to $output_file" 