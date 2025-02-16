#!/bin/bash
#Check if atleast one argument is provided
if [ $# -eq 0 ]; then
   echo "usage: $0 <path_name>"
exit 1
fi
#Enter the path as input
path_name="$1"
#Check if the given path is a directory
if [ -d $path_name ]
then
  echo "It is a directory"
#check if a given path is a file
elif [ -f $path_name ]
then
  echo  "It is a file"
fi
