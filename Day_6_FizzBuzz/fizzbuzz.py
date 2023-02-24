import os


def clear_screen():
    return os.system("clear || cls")


def menu():
    clear_screen()
    print("Welcome to FizzBuzz! All numbers are between 0 and 50.")

    while True:
        user_input = input(
            "\nWhat would you like to do?"
            "\n- Enter 'fizz' to see numbers divisible by 3"
            "\n- Enter 'buzz' to see numbers divisible by 5"
            "\n- Enter 'fizzbuzz' to see numbers divisible by 3 AND 5"
            "\n- Enter 'all' to see every number"
            "\n- Enter 'clear' to clear the terminal screen"
            "\n- Enter 'quit' to exit the program: "
        ).lower()

        if user_input == 'fizz':
            clear_screen()
            print(f"Fizzy numbers (divisible by 3): {[number for number in range(0,51) if number % 3 == 0]}")
        elif user_input == 'buzz':
            clear_screen()
            print(f"Buzzy numbers (divisible by 5): {[number for number in range(0,51) if number % 5 == 0]}")
        elif user_input == 'fizzbuzz':
            clear_screen()
            print(f"FizzBuzzy numbers (divisible by 3 AND 5): {[number for number in range(0,51) if number % 3 == 0 and number % 5 == 0]}")
        elif user_input == 'all':
            clear_screen()
            for number in range(0,51):
                if number % 3 == 0 and number % 5 == 0:
                    print(f"{number} - FizzBuzz")
                elif number % 3 == 0:
                    print(f"{number} - Fizz")
                elif number % 5 == 0:
                    print(f"{number} - Buzz")
                else:
                    print(number)
        elif user_input == 'clear':
            clear_screen()
        elif user_input == 'quit':
            clear_screen()
            print("\nThank you for using FizzBuzz. I hope you have a great day!\n")
            break
        else:
            clear_screen()
            print("Please enter a valid input.")



menu()