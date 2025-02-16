#!/bin/bash
age="$1"
if(( $age > 120 ))
then
   echo "invalid input"
else
  echo "You are an adult"
fi


