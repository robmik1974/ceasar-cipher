def caesar(text: str, offset: int, direction: str):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k",
                "l","m","n","o","p","q","r","s","t","u","v",
                "w","x","y","z"," "]

    caesar_text = ""

    if direction == "encode":
        for letter in text:
            caesar_text += alphabet[(alphabet.index(letter) + offset) % 27]
    elif direction == "decode":
        for letter in text:
            caesar_text += alphabet[(alphabet.index(letter) - offset) % 27]

    return caesar_text


def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(caesar(text=text, offset=shift, direction=direction))


if __name__ == "__main__":
    main()
