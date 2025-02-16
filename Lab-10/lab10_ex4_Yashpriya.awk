#Convert degree celsius to fahrenheit
{ cel=$1;
fah=cel * 1.8 + 32;
printf "Temperature in fahrenheit for input celsius %d is %f\n", cel, fah}
