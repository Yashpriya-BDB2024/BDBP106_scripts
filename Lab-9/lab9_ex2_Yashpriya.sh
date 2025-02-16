#!/bin/bash
check_num_range() { 
read -p "Enter the number:" num
if [ $num -ge 10 ] && [ $num -le 20 ]
then
  echo "The number $num lies between 10 and 20"
else
  echo "The number $num does not lie between 10 and 20"
fi 
}
check_num_range
