#!/bin/bash
while true
do
echo "What would you like to do today
1. List Files
2. List Processes
3. See list of users
4. Exit to Unix shell"
read choice
case $choice in
  1) ls -l ;;
  2) ps -f ;;
  3) who ;;
  4) exit ;;
  *) echo "invalid option"
esac
done 
