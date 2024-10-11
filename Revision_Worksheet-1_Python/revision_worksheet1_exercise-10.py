def replace(S):
    replaced_S=S.replace(',', ' and')  #This will replace ',' with 'and'
    return replaced_S
def main():
    S=input("Enter word1, word2: ")
    result=replace(S)
    print(f"The output after replacing the ',' in {S} is {result}")
if __name__ == "__main__":
    main()