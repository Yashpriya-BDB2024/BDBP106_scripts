#!/bin/bash
#check if atleast one argument is provided
if [ $# -eq 0 ]; then
  echo "usage: $0 number1 number2----numberN"
  exit 1
fi
#initializing sum to zero
sum=0
#loop through all the arguments
for num in "$@"; do 
#Add the current number to the sum
sum=$(( sum + num ))
done
#print the result
echo "The sum of the numbers is : $sum" 
