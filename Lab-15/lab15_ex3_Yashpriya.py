#Get the name of the month as input
month=str(input("Enter the month: "))
#Set days as default empty string
days=""
#Check the number of days present in the given month
if month=="January":
    days="31 days"
elif month=="February":
    days="28 or 29 days" 
elif month=="March":
    days="31 days"
elif month=="April":
    days="30 days"
elif month=="May":
    days="31 days"
elif month=="June":
    days="30 days"
elif month=="July":
    days="31 days"
elif month=="August":
    days="31 days"
elif month=="September":
    days="30 days"
elif month=="October":
    days="31 days"
elif month=="November":
    days="30 days"
elif month=="December":
    days="31 days"
else:
    print('Error')
#Print the output statement
print("The number of days in", month, "is", days) 
