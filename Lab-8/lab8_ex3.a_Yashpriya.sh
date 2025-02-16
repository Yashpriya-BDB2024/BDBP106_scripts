#!/bin/bash
read -p "Enter the number:" num
if (( $num == 1 ))
then
   echo "$num is a unique number"
else
   exit;
fi
#By using while loop -
read -p "Enter the number:" number
prime=TRUE
i=2
while [ $i -lt $number ]
do
  if (( number%i == 0 ))
  then
     echo $i
     prime=FALSE
     break;
else
   i=$(( i +1 ))
fi
done
echo "The number $number is a prime number: $prime" 
