#!/bin/bash
Sum=$(( $1 +$2 ))
echo "Sum of $1 and $2 is $Sum"
Product=$(( $1 *$2 ))
echo "Product of $1 and $2 is $Product" 
Quotient=$(( $1 /$2 )) 
echo "Quotient of $1 and $2 is $Quotient"
Remainder=$(( $1 %$2 ))
echo "Remainder of $1 and $2 is $Remainder"
