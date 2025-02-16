#To find the total expenses
BEGIN {sum=0}
{sum=sum+$2}
END {
printf "The total expenses is %d\n", sum } 
