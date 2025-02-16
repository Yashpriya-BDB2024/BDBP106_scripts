# To determine whether or not a password is good.
def is_good_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    return has_upper and has_lower and has_digit
def main():
    password = input("Enter a password: ")
    if is_good_password(password):
        print(f"The generated password '{password}' is good.")
    else:
        print(f"The generated password '{password}' is not a good one.")
if __name__ == "__main__":
    main()