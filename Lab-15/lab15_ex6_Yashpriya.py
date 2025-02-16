#Get the year as input from the user
year=int(input("Enter a year that is equal to or greater than 0: "))
if year < 0:
    print('Error')
#Calculate the position in the zodiac cycle
position=year%12
#Set default empty string
animal=""
#Now, determine the zodiac animal based on the calculated position
if position==0:
    animal="Monkey"
elif position==1:
    animal="Rooster"
elif position==2:
    animal="Dog"
elif position==3:
    animal="Pig"
elif position==4:
    animal="Rat"
elif position==5:
    animal="Ox"
elif position==6:
    animal="Tiger"
elif position==7:
    animal="Hare"
elif position==8:
    animal="Dragon"
elif position==9:
    animal="Snake"
elif position==10:
    animal="Horse"
elif position==11:
    animal="Sheep"
else:
    print(error)
print('%d is the year of the %s' %(year, animal))

    
