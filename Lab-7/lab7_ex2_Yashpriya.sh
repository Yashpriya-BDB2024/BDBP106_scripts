#!/bin/bash
read -p "Enter your age" age
if(( $age < 18 ))
then
   echo "You are a child"
else
   echo "You are an adult"
fi
