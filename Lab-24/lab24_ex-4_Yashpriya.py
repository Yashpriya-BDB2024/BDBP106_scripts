x=17
def checkNameSpaces():
    z=12
    x=2002
    print(f"Global name-space: {globals()}")
    print(f"Local name-space: {locals()}")
def main():
    checkNameSpaces()
if __name__ == "__main__":
    main()