def display_key_presses(message):
    key_presses_dict = {
        ".": "1", ",": "11", "?": "111", "!": "1111", ":": "11111",
        "A": "2", "B": "22", "C": "222",
        "D": "3", "E": "33", "F": "333",
        "G": "4", "H": "44", "I": "444",
        "J": "5", "K": "55", "L": "555",
        "M": "6", "N": "66", "O": "666",
        "P": "7", "Q": "77", "R": "777", "S": "7777",
        "T": "8", "U": "88", "V": "888",
        "W": "9", "X": "99", "Y": "999", "Z": "9999",
        " ": "0"
    }
    message=message.upper()
    result=''.join([key_presses_dict[char] for char in message if char in key_presses_dict])   # ''.join - to concatenate strings
    return result
def main():
    message=input("Enter a message: ")
    print(display_key_presses(message))
if __name__ == "__main__":
    main()
