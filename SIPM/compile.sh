#!/bin/bash

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
while IFS= read -r directory;
do
    echo "running $line"
    OUTPUT_FILENAME="./$directory/mean_sd_compiled.txt"
    FIRST_FILE="./$directory/mean_sd_1_2_3_4.txt"
    SECOND_FILE="./$directory/mean_sd_5_6_7_8.txt"
    THIRD_FILE="./$directory/mean_sd_9_10_11_12.txt"
    FOURTH_FILE="./$directory/mean_sd_13_14_15_16.txt"
    cp  $FIRST_FILE $OUTPUT_FILENAME
    tail -n +2 $SECOND_FILE >> $OUTPUT_FILENAME
    tail -n +2 $THIRD_FILE >> $OUTPUT_FILENAME
    tail -n +2 $FOURTH_FILE >> $OUTPUT_FILENAME
done < "$filename"

