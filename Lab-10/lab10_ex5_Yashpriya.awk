#Print the names of all the employees whose age is more than 30 years 
BEGIN {FS=","}
$3 > 30 {print $1}
END { print "Done" } 
