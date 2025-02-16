#!/bin/bash
# Check if atleast two arguments are provided 
if [ $# -eq 0 ]; then 
  echo "Usage: $0 <directory_name> <file_name>"
  exit 1
fi
# Assign input parameters to variables
Dir_name="$1"
File_name="$2"
# Create the directory
mkdir -p "$Dir_name" 
# Create the file and write content into it
echo "This is a test file" > "$Dir_name/$File_name" 
# Display the content of the file
cat "$Dir_name/$File_name" 
