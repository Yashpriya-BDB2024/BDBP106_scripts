def reverse_str(Dict):
    reverse_string=lambda s: s[::-1]  # reverses the string as key
    reverse_check=[print(f"{key}: {'True' if reverse_string(key) == val else 'False'}") for key, val in Dict.items()]  # if the reversed key is same as value, then true, otherwise, false (for each item in the dictionary).
    return reverse_check

def main():
    Dict={"hello": "olleh", "python": "language", "world": "dlrow", "1234": "4321", "#$?%": "$%#?"}
    reverse_str(Dict)
if __name__ == "__main__":
    main()