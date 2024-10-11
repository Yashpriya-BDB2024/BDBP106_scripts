def article_usage(word):
    vowels="aeiou"
    if word[0] in vowels:
        return "an"
    else:
        return "a"
def main():
    word=input("Enter a word: ")
    result=article_usage(word)
    print(f"The {word} is prefixed by {result}")
if __name__ == "__main__":
    main()
