hundred_ones_place={1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
# Nested dictionary with key as '1' representing the 'tens' place & inside it are the 'ones' places.
teen_place={1:
                {0:'ten', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen'}
            }
ty_places={2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

def eng_words(N):
# If the input is zero, then there is no need to calculate t_n, h_n, so handled separately.
    if N==0:
        print("Zero")
    h_n=N//100
    t_n=(N%100)//10
    u_n=(N%10)//1
# Initializing an empty string to store the following output.
    words=""
# Checking if there is a hundred place in the given no., if yes, then retrieve the value from its respective dictionary with the key as its calculated 'h_n'; also capitalize the output.
# The word "Hundred" is appended after the output is appended in the empty string.
    if h_n>0:
        words += hundred_ones_place[h_n].capitalize() + " Hundred "
        if t_n>0 or u_n>0:
            words += "and "
# If tens place is 1 and ones place is 0, then only it will print 'Ten'.
# Otherwise, it will retrieve the value from 'teens' dictionary as per the calculated 'u_n' (since, it is nested dict., so we need both the keys as t_n & u_n).
    if t_n==1:
        if u_n==0:
            words += "Ten"
        else:
            words += teen_place[t_n][u_n].capitalize()
# If 'tens' place has a no. greater than 1, then it will look into 'ty' dictionary (for 20, 30, 40, ......, 90)
    elif t_n>1:
        words += ty_places[t_n].capitalize() + " "
# If units place has a no. greater than 0, then, it needs value from 'ones' dictionary as well.
        if u_n>0:
            words += hundred_ones_place[u_n].capitalize()
# If tens place has 0, & units place has a no. that is greater than 0, then again it looks into 'hundred_ones_place' dictionary.
    elif t_n==0 and u_n>0:
        words += hundred_ones_place[u_n].capitalize()
    print(words)

def main():
    N=int(input("Enter a number between 0 and 999: "))
# This is to handle negative numbers or the numbers that are greater than 999.
    if N<0 or N>999:
        print("Please enter a number between 0 and 999")
        return
    else:
        eng_words(N)
if __name__ == "__main__":
    main()
