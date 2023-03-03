import os
import random
from art import logo


os.system("clear || cls")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for character in start_text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += character
    print(f"\nHere's the {cipher_direction}d result: {end_text}")


print(logo)

should_end = False

while not should_end:
    direction = input("\nEnter 'encode' to encrypt or enter 'decode' to decrypt: ")
    text = input("Enter your message: ").lower()
    shift = int(input("Enter the shift number: "))

    shift = shift % 26
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("\nEnter 'yes' to go again or 'no' to exit the program: ")
    if restart == "no":
        should_end = True
        os.system("clear || cls")
        print("\nGoodbye.\n")