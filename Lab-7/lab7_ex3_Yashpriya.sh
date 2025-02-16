#!/bin/bash
read -p "Enter the name of a directory" dir
if [ -d $dir ]
then
   echo "Directory $dir exists"
else
   echo "Directory $dir does not exists"
fi 

#To check whether file exists or not
read -p "Enter the name of a file" file
if [ -f $file ]
then
   echo "File $file exists"
else
   echo "File $file does not exists"
fi

#modified version-a
read -p "Enter the name of the file or directory" check
if [ -e $check ]
then
   echo "Directory or file exists"
else
   echo "Directory or file does not exists"
fi 

#modified version-b
read -p "Enter the name of a directory" dir 
if [ -f $dir ] 
then
   echo "Directory $dir exists" 
else
  echo "Directory $dir does not exists" 
fi
