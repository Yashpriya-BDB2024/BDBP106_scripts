#!/bin/bash
#check if atleast one argument is provided
if [ $# -eq 0 ]; then
echo "usage: $0 number" 
exit 1 
fi
#get the input number
number=$1
#check if the given number has three or more digits
if [ ${#number} -lt 3 ]
then
  echo "Enter the number having 3 or more than 3 digits"
  exit 1
fi 
#initialize the sum to zero
sum=0
#loop through each digit in a given number
while [ $number -gt 0 ]; do
#get last digit
digit=$(( number % 10 ))
#add digit to the sum
sum=$(( sum + digit ))
#remove the last digit from the number
number=$(( number / 10 ))
done
#print the result
echo "The sum of all the digits in the given number is: $sum" 
