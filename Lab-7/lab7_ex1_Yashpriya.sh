#!/bin/bash
read -p "Enter the temperature in Celsius:" Celsius
fah=$(($Celsius*9))
fah=$(($fah/5))
fah=$(($fah + 32))
echo "Temperature in Fahrenheit:$fah F" 

#Convert Fahrenheit into Celsius
read -p "Enter the temperature in Fahrenheit:" Fahrenheit
cel=$(($Fahrenheit-32))
cel=$(($cel*5))
cel=$(($cel/9))
echo "Temperature in Celsius:$cel C" 
