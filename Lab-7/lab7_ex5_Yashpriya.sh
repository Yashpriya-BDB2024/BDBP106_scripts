#!/bin/bash
#modified version-b, i.e., copying only files but not the directories
for file in `ls ${pwd}` 
do
    cp $file ${file}.bak
    echo "copied $file"
done 

#To copy both files and directories
for file in `ls ${pwd}`
do
  cp -r $file ${file}.bak
  echo "copied $file"
done
