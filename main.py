from caesar_art import logo
import os

def caesar(text: str, offset: int, direction: str):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k",
                "l","m","n","o","p","q","r","s","t","u","v",
                "w","x","y","z"]

    caesar_text = ""

    for letter in text:
        if letter in alphabet:
            if direction == "encode":
                caesar_text += alphabet[(alphabet.index(letter) + offset) % 26]
            elif direction == "decode":
                caesar_text += alphabet[(alphabet.index(letter) - offset) % 26]
        else:
                caesar_text += letter

    return caesar_text


def main():
    os.system('clear')
    print(logo)
    should_stop = False
    while not is_stopped:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        print(caesar(text=text, offset=shift, direction=direction))
        answer = input("Type 'no' if you want to stop, otherwise type any key.").lower()
        if answer == 'no':
            should_stop = True
            print("Goodbye")



if __name__ == "__main__":
    main()
