#!/bin/bash
#check if atleast one argument is provided
if [ $# -eq 0 ]; then
echo "usage: $0 <gzip_file_name: without extension>"
exit 1
fi
#get the gzip file name from the argument
gzip_name="$1"
#check if it is an existing gzip file
if [ -e $gzip_name.tar.gz ]; then
#unzip or uncompress the given file
gunzip $gzip_name.tar.gz
echo "List of files in tar file"
tar -tf $gzip_name.tar
echo "Doing untar"
tar -xvf $gzip_name.tar
else
echo "Enter correct file name" 
fi
echo "exit code: $?"
