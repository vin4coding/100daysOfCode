alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(direction, text, shift):
    end_txt = ""
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = position + shift
            end_txt += alphabet[new_pos]
        else:
            end_txt += char
    return print(f'The {direction}d string is {end_txt}')


if __name__ == "__main__":
    should_continue = True
    while should_continue:
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        text = input("Type your message:\n").lower()

        shift = int(input("Type the shift number:\n"))
        caeser(direction, text, shift)
        run_again = input(
            "If you want to run again press 'Yes' or press 'No' to Quit: \n ")
        if run_again.lower() == "no":
            should_continue = False
            print("Good Bye!")
        elif run_again.lower() == "yes":
            should_continue = True
