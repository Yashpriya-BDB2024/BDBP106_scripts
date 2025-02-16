#!/bin/bash
age="$1"
if(( $age < 18 )) 
then
   echo "You are a child"
else
  echo "You are an adult"
fi

