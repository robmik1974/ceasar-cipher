def encrypt(text_to_encrypt: str, offset: int):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k",
                "l","m","n","o","p","q","r","s","t","u","v",
                "w","x","y","z"," "]

    encrypted_text = ""

    for letter in text_to_encrypt:
        encrypted_text += alphabet[(alphabet.index(letter) + offset) % 27]

    return encrypted_text


def decrypt(text_to_decrypt: int, offset: int):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k",
                "l","m","n","o","p","q","r","s","t","u","v",
                "w","x","y","z"," "]

    decrypted_text = ""

    for letter in text_to_decrypt:
        decrypted_text += alphabet[(alphabet.index(letter) - offset) % 27]

    return decrypted_text


def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(encrypt(text_to_encrypt=text, offset=shift))
    elif direction == "decode":
        print(decrypt(text_to_decrypt=text, offset=shift))
    else:
        print("Incorect type of action!")


if __name__ == "__main__":
    main()
