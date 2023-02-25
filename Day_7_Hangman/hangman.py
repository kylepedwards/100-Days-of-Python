import os 
import random
from hangman_words import word_list
from hangman_art import logo 
from hangman_art import stages


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

os.system("clear || cls")

print(logo)
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print(f"\nYou've already guess {guess}.")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose.\n")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\nYou win.\n")
    
    print(stages[lives])