import os 


def clear_screen():
    return os.system("clear || cls")


clear_screen()

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island! Your mission is to find the treasure.\n")

choice_1 = input("You were walking on a trail and came to a fork in the road.\nDo you go 'left' or 'right'? ").lower()

if choice_1 == "left":
    clear_screen()
    choice_2 = input(
        "You went left."
        "\nAfter walking down that trail for some time, you found a lake with an island in the middle of it."
        "\nDo you 'wait' for a boat to come by or do you try to 'swim' across? "
    ).lower()
    if choice_2 == "wait":
        clear_screen()
        choice_3 = input(
            "You waited. After some time a boat came, dropped you off on the island, and disappeared."
            "\nYou find a house with three doors - one red door, one blue door, and one yellow door."
            "\nWhich door do you go through? "
        ).lower()
        if choice_3 == "red":
            print("\nYou opened the red door, was sucked into a room engulfed in flames, and burned to death. GAME OVER!\n")
        elif choice_3 == "yellow":
            print("\nYou opened the yellow door and found a room full of treasure! MISSION ACCOMPLISHED! YOU WIN!\n")
        elif choice_3 == "blue":
            print("\nYou opened the blue door, was sucked into a room full of wicked beasts, and was torn to shreds. GAME OVER!\n")
        else:
            print("\nYou chose a door that doesn't exist. You were teleported into outer space and died. GAME OVER!\n")
    else:
        print("\nYou tried to swim across. Suddenly, you were attacked by a giant angry trout and drowned. GAME OVER!\n")
else:
    print("\nYou went right. After a while, you fell into a hole and were beaten up by angry gophers. GAME OVER!\n")
