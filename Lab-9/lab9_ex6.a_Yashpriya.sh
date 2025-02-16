#!/bin/bash
#Take input 'n' from the user
read -p "Enter the number of terms:" n
#Initialize the first two fibonacci numbers to 0 and 1 respectively 
a=0
b=1
#check if the number is a positive integer
if [ $n -le 0 ]
then
   echo "enter positive integer"
exit 1
fi
#print the fibonacci series
for (( i=0 ; i<n ; i++ ))
do
echo -n " $a "
  sum=$(( a + b ))
a=$b
b=$sum
done
echo 
