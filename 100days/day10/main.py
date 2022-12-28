import os
from art import logo

def add(n1, n2):
    """Return n1 + n2"""
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
        '+' : add,
        '-' : subtract,
        '*' : multiply,
        '/' : divide,
        }

def calculator():
    os.system('cls')
    print(logo)

    num1 = float(input("What's your first number: "))
    for symbol in operations:
        print(symbol)
    should_continues = True
    while should_continues:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input("What's your next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continues = False
            os.system("cls")
            calculator()

calculator()
