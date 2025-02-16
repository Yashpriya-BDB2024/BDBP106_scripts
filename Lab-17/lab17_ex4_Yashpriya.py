#Import the get_ordinal function from the file called lab17_ex3_Yashpriya
from lab17_ex3_Yashpriya import get_ordinal
def display_verse(num):
#Print the introductory line with the ordinal day
    print("On the", get_ordinal(num), "day of Christmas, I got")
    if num >= 5:
        print("five golden rings,")
    if num >= 4:
        print("four calling birds,")
    if num >= 3:
        print("three French hens,")
    if num >= 2:
        print("two turtle doves,")
    if num == 1:
        print("a partridge in a pear tree")
    else:
        print(",and a partridge in a pear tree")
def main():
#Loop through the first 5 days and display each verse
    for i in range(1, 6):
        display_verse(i)
#Add a blank line for better separation between verses
        print()
if __name__ == "__main__":
    main()
