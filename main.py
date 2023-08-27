# importing the logo
from logo import logo

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Making a function that encrypts or decrypts the message
def caesar(user_text, shifting_num, e_or_d):
    result = ""
    if e_or_d == "decode":
        shifting_num *= -1

    # Shifting the letters of the text
    for letter in user_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position + shifting_num
            result += alphabets[new_position]

        else:
            result += letter
    print(f"Here's the {e_or_d}d result: {result}")

# Printing the logo
print(logo)


u_input = False
while not u_input:
    # Asking to encrypt or decrypt the message
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Receiving the message
    text = input("Type your message:\n").lower()
    # Asking for the no. of shift amount
    shift = int(input("Type the shift number:\n"))
    # Making sure that the shift does not exceed the no. of alphabets
    shift = shift % 26
    # Calling the function
    caesar(text, shift, direction)

    # Asking if they want to use this again
    user_input = input("Type 'yes' if you want to use this again. Otherwise type 'no'.")
    if user_input == "no":
        u_input = True
        print("Goodbye")

