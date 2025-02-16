def capitalize_string(s):
#Capitalize the first character
    s = s[0].upper() + s[1:]
    words = s.split()
    for i in range(len(words)):
#Capitalize I if its surrounded by spaces.
        if words[i] == "i":
            words[i] = "I"
# Capitalize the first word after a punctuation mark
        if i > 0 and words[i - 1].endswith(('.', '!', '?')):
            words[i] = words[i].capitalize()
    return ' '.join(words)
def main():
    string=input("Enter a string: ")
    result=capitalize_string(string)
    print(result)
if __name__ == "__main__":
    main()