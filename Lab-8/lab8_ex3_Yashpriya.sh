#!/bin/bash
read -p "Enter the number:" num
prime=TRUE
for (( i=2; i<num; i++ ))
do
  if (( num%i == 0 ))
  then
     echo $i
     prime=FALSE
     break;
else
   continue;
fi
done
echo "The number $num is a prime number: $prime" 
