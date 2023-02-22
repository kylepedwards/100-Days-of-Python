import os
import random


os.system("clear || cls")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input(
    "What do you want to choose?"
    "\nEnter 0 for Rock,"
    "\n1 for Paper,"
    "\nor 2 for Scissors: "
))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: {game_images[computer_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("\nYou entered an invalid option. YOU LOSE!\n")
elif user_choice == 0 and computer_choice == 2:
    print("\nYOU WIN!\n")
elif computer_choice == 0 and user_choice == 2:
  print("\nYOU LOSE!\n")
elif computer_choice > user_choice:
  print("\nYOU LOSE!\n")
elif user_choice > computer_choice:
  print("\nYOU WIN!\n")
elif computer_choice == user_choice:
  print("\nDRAW!\n")