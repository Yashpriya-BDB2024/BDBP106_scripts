def friends_info(fr_list,clg_list,no_frs):
#Make a dictionary
    friends_colleges={}
    for i in range(no_frs):
#Usage: dict[key]=value
        friends_colleges[fr_list[i]]=clg_list[i]
#Get values, i.e., list of colleges
    frnd_clg=(list(friends_colleges.values()))
    print(f"UG college names: {frnd_clg}")

def details():
    name = input("Enter name: ")
    email_address = input("Enter email-address: ")
    age = int(input("Enter the age: "))
#Make tuples of details
    friends_details = (name, email_address, age)
    return friends_details

def main():
    num_of_friends = int(input("Enter the no. of friends you have: "))
#Make a list of tuples
    friends_tuples=[]
#Make a list of college names
    college_list = []
#Each time it iterates (till the given value of no. of friends), it will do the following operations - calling the details(), etc.
    for i in range(num_of_friends):
#Calling the function 'details()' & storing the output in 'f'
        f=details()
        college = input("Enter UG college name: ")
#Appending the output present in 'f' in the list 'friends_tuples'
        friends_tuples.append(f)
#Appending the college names in the list 'college_list'
        college_list.append(college)

    result=friends_info(friends_tuples,college_list,num_of_friends)
    print(result)

if __name__ == "__main__":
    main()
