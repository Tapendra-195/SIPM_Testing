#!/bin/bash                                                                     

# Check if a filename is provided as an argument                                                                                              
if [ $# -lt 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename=$1

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "File $filename not found."
    exit 1
fi

# Read the file line by line
while IFS= read -r line;
do
    echo "running $line"
    python3 get_mean_sigma.py "1_2_3_4_fc.csv" "./$line/"
    python3 get_mean_sigma.py "5_6_7_8_fc.csv" "./$line/"
    python3 get_mean_sigma.py "9_10_11_12_fc.csv" "./$line/"
    python3 get_mean_sigma.py "13_14_15_16_fc.csv" "./$line/"
done < "$filename"
