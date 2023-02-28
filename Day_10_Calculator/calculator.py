import os


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    os.system("clear || cls")
    number1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(number1, number2)
        print(f"\n{number1} {operation_symbol} {number2} = {answer}")

        if input(f"\nEnter 'yes' to continue calculating with {answer} or 'no' to start a new calculation: ") == "yes":
            number1 = answer
        else: 
            should_continue = False
            os.system("clear || cls")
            calculator()


calculator()