class AgeTooYoungError(Exception):
    pass
def checkAge(age):
    try:
        if age<18:
            raise AgeTooYoungError("Age must be more than 18")
        else:
            print("Age is more than 18")
    except AgeTooYoungError as err:
        print(f"Error: {err}")
def main():
    try:
        checkAge(3)
    except ValueError:
        print("Enter only integers.")
if __name__ == "__main__":
    main()
