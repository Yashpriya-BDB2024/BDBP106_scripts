#!/bin/bash
#check if atleast one argument is provided
if [ $# -eq 0 ]; then
  echo "usage: $0 <file_name>"
exit 1
fi
#get file name from argument and display its original contents 
file_name="$1"
#get specific word from argument in order to search it in the given file
word="$2"
#search the given word in the file
if ! grep -q "$word" "$file_name"; then
echo "No occurrences of $word in $file_name"
exit 1
else 
#get the word that replaces the above word 
rep_word="$3"
#replace the word with new one
sed -i "s/$word/$rep_word/g" "$file_name" 
fi
#display the contents of the given file
cat $file_name 
echo "modified successfully"

