#!/bin/bash
read -p "Enter the number of terms:" n
a=1
b=1
#declaring the function
fib (){
   local i
   i=$1
   if (( i <=1 )); then
     echo "$i" 
   else
     echo $(( $(fib $((i-1)) ) + $(fib $((i-2))) ))
   fi
}
echo "Fibonacci series:"
for (( j=1; j<=$n; j++ )); do
fib $j
done
