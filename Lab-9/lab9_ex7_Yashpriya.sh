#!/bin/bash
echo "Select the operations from the following
1. count the number of lines 
2. replace a with A in the file
3. count the number of occurrences of "the" in the file" 
read choice
case $choice in
  1) read -p "Enter the name of a file:" file
     num_of_lines=$(wc -l < $file) 
     echo "The number of lines in $file is $num_of_lines" ;; 
  2) read -p "Enter the name of a file:" file
    replacement=$(sed -i 's/a/A/g' $file) ;; 
  3) read -p "Enter the name of a file:" file
     num_of_occurrences=$(grep -i 'the' $file | wc -l) 
     num_of_occurr=$(grep -io 'the' $file | wc -l)
    echo "The number of occurrences of the is $num_of_occurr" ;; 
  4) exit ;;
  *) echo "invalid option"
esac 

      
