#modify the value of banana from 100 to 150
{
#check if the first field is Banana and second field is 100
if (($1=="Banana") && ($2==100)) {
#change the value to 150
$2=150
}
#print the modified version of file
print
}
