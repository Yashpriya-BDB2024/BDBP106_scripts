#!/bin/bash
BEGIN {
#Initialize maximum value to zero
max_value=0
#Initialize minimum value to infinity
min_value=1/0 
}
#check if the value present in second field is greater than the current max_value
{
if ($2>max_value) {
#update the max_value
max_value=$2 }
#check if the value present in second field is lesser than the current min_value
if ($2<min_value) {
#update the min_value
min_value=$2 }
}
#print the max_value and min_value present in second field
END { print "max_value:" max_value, "min_value:" min_value 
}
