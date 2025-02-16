#Print the names of all the employees who lives in India 
BEGIN {FS=","} 
$4=="India" {printf "%s lives in %s\n",$1,$4}
END {print "Done"}

