#Get the plain text message from the user as input
message=input('Enter the plain text message: ')
#Get the shift integer as input
shift_integer=int(input('Enter the shift integer'))
#Set the default empty string
new_message=""
for ch in message:
    if 'a' <= ch <= 'z':
        pos=ord(ch)-ord('a')
        pos=(pos+shift_integer)%26
        new_char=chr(pos+ord('a'))
        new_message=new_message+new_char
    elif 'A' <= ch <= 'Z':
        pos=ord(ch)-ord('A')
        pos=(pos+shift_integer)%26
        new_char=chr(pos+ord('A'))
        new_message=new_message+new_char
    else:
        new_message=ch
#Print the output statement
print('The new message is:', new_message)