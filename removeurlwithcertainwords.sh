#!/bin/bash

input_file="$1"
output_file="${input_file%.txt}_filtered.txt"

if [ ! -f "$input_file" ]; then
  echo "Error: Input file not found."
  exit 1
fi

while IFS= read -r line; do
  if [[ $line != *"shop"* ]]; then  
    echo "$line" >> "$output_file"
  fi
done < "$input_file" 
  
echo "URLs with 'shop' keyword removed and saved to $output_file"
  
  
