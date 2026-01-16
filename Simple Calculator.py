import math

print("Welcome To My Simple Calculator! Calculation of upto 2 digits can only be performed.")
print("""Choose the symbol from below to perform calculation.
Addition ==> + 
Subtraction ==> -
Multiplication ==> *
Division ==> /
Exponent ==> **
square root ==> sqrt
exit ==> !""")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def exponent(a, b):
    return a ** b


symbols = {"+": add, "-": subtract, "*": multiply, "/": divide, "**": exponent}


while True:
    symbol = input("Enter the symbol for calculation: ")
    if symbol == "!":
        print("Exited Successfully!")
        break

    if symbol == "sqrt":
        try:
            num = float(input("Enter the number to find the square root: "))
            print(math.sqrt(num))
        except ValueError:
            print("Invalid Input. Enter numbers only")
        continue

    if symbol not in symbols:
        print("Enter a valid symbol.")
        continue

    try:
        num1 = float(input("Enter first digit: "))
        num2 = float(input("Enter second digit: "))
        if num2 == 0 and symbol == "/":
            print("Cannot be divided by zero")
            continue
    except ValueError:
        print("Invalid Input. Enter numbers only")
        continue

    result = symbols[symbol](num1, num2)
    print(f"Result: {result}")


