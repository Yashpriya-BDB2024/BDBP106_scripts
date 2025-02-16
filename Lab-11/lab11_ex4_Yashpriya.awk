BEGIN {FS=","}
{
#Get the names of actresses who won Oscar before 1965 and print the following statement 
if (($2 < 1965) && (NR > 1))
{
    printf "%s won an oscar in %d when she was %d for the movie %s\n", $4, $2, $3, $5
}
}
