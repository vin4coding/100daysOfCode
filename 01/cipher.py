alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))


def caeser(direction, text, shift):
    cipher = ""
    if shift > 25:
        shift = shift-26
    if direction == 'decode':
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_pos = position + shift
        cipher += alphabet[new_pos]
    return f'The {direction}d string is {cipher}'


if __name__ == "__main__":
    print(caeser(direction, text, shift))
