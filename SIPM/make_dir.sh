!#!/bin/bash

# Loop from 1 to 21
for i in {1..21}
do
  # Format the folder name with leading zero if needed
  folder_name=$(printf "UWPG%02d" $i)
  
  # Create the folder
  mkdir $folder_name
  
  # Print a message indicating the folder has been created
  echo "Created folder: $folder_name"
done
