#print last names
{
if (NF>1) {
if (NR==1) {printf "%s\n", $2}
if (NR==2) {printf "%s\n", $3}
if (NR==3) {printf "%s\n", $3}
if (NR==4) {printf "no last name", $1} 
if (NR==5) {printf "%s\n", $4}
}
else {
print "no last name:" $0
}
}
