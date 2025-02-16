#!/bin/bash
echo "What would you like to do today
1. Addition 
2. Subtraction
3. Multiplication 
4. Quotient
5. Remainder" 
read -p "Enter your choice:" choice 
read -p "Enter the first number:" a 
read -p "Enter the second number:" b 
case $choice in
  1)result=$(( $a + $b )) 
          echo "The sum of $a and $b is $result" ;; 
  2)result=$(( $a - $b )) 
           echo "The difference of $a and $b is $result" ;; 
  3)result=$(( $a * $b )) 
           echo "The product of $a and $b is $result" ;; 
  4)result=$(( $a / $b ))
          echo "The quotient when $a is divided by $b is $result" ;; 
  5)result=$(( $a % $b )) 
          echo "The remainder when $a is divided by $b is $result" ;;
  *)echo "invalid option"
esac 
