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
    python3 plot.py "1_2_3_4.csv" "./$line/"
    python3 plot.py "5_6_7_8.csv" "./$line/"
    python3 plot.py "9_10_11_12.csv" "./$line/"
    python3 plot.py "13_14_15_16.csv" "./$line/"
done < "$filename"