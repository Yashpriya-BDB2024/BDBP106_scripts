#!/bin/bash
#check if atleast one argument is provided
if [ $# -eq 0 ]; then
  echo "usage: $0 <dir_name>"
exit 1
fi
#Get the directory name from argument
dir_name="$1"
#check if the input provided is a directory that exists
if [ -d $dir_name ]; then
cd $dir_name
#Archive all the files present in the given directory
tar -cvf $dir_name.tar ./*
#Show the size of tar file before compression 
size_before=$(ls -lh $dir_name.tar | awk '{print $5}')
echo "Size of the tar file before compression is $size_before"
#Compress the tar file 
gzip $dir_name.tar
#show the size of tar file after compression
size_after=$(ls -lh $dir_name.tar.gz | awk '{print $5}')
echo "Size of compressed tar file is $size_after" 
else
echo "Give the correct existing directory name"
fi
echo "Exit code: $?"
