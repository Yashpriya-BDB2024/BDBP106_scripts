#print the sum of all numbers present in the rand_num.csv
BEGIN {sum=0}
{sum=sum+$1}
END{
print sum}
