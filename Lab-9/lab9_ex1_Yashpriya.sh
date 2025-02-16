#!/bin/bash
#check if a given number is odd or even
read -p "Enter the number:" num
if (( $num%2 == 0 ))
then
   echo "$num is an even number"
elif (( $num%2 == 1 ))
   then
     echo "$num is an odd number"
fi
 
