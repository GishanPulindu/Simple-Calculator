import math
import tkinter


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


def cli_cal():
    print("Welcome To My Simple Calculator! Calculation of upto 2 digits can only be performed.")
    print("""Choose the symbol from below to perform calculation.
    Addition ==> + 
    Subtraction ==> -
    Multiplication ==> *
    Division ==> /
    Exponent ==> **
    square root ==> sqrt
    exit ==> !""")

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


current_input = ""

def gui_cal():

    def press_button(char):
        global current_input
        current_input += str(char)
        display_var.set(current_input)

    def calculate():
        global current_input
        try:
            result = str(eval(current_input))
            display_var.set(result)
            current_input = result
        except ZeroDivisionError:
            display_var.set("Cannot divide by zero")
            current_input = ""
        except (SyntaxError, NameError):
            display_var.set("Invalid Expression")
            current_input = ""
        except Exception:
            display_var.set("Invalid Input")
            current_input = ""

    def clear():
        global current_input
        current_input = ""
        display_var.set(current_input)

    root = tkinter.Tk()
    root.title("My Calculator")
    root.geometry("350x450")

    display_var = tkinter.StringVar()
    display = tkinter.Entry(root, textvariable=display_var, bd=5, font=("Arial", 18), relief="sunken", justify='right', state='readonly')
    display.grid(row=0, column=0, columnspan=5, sticky="nsew")

    operations = [("+", 1, 0), ("-", 1, 1), ("*", 1, 2), ("/", 1, 3), ("**", 1, 4)]
    numbers = [("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("4", 2, 3), ("5", 2, 4), ("6", 3, 0), ("7", 3, 1), ("8", 3, 2), ("9", 3, 3), ("0", 3, 4)]

    for text, r, c in numbers:
        b1 = tkinter.Button(root, text=text, command=lambda t=text: press_button(t), font=("Arial", 18), relief="ridge")
        b1.grid(row=r, column=c, sticky="nsew")
    for text, r, c in operations:
        b = tkinter.Button(root, text=text, command=lambda t=text: press_button(t), font=("Arial", 18), relief="ridge")
        b.grid(row=r, column=c, sticky="nsew")

    tkinter.Button(root, text="=", font=("Arial",18), relief="ridge", command=lambda: calculate()).grid(row=4, column=0, sticky="nsew")
    tkinter.Button(root, text="Clear", font=("Arial", 18), relief="ridge", command=lambda: clear()).grid(row=4, column=1, columnspan=4, sticky="nsew")

    for i in range(5):
        root.rowconfigure(i, weight=1)
    for j in range(5):
        root.columnconfigure(j, weight=1)


    root.mainloop()


if __name__ == "__main__":
    gui_cal()
    # cli_cal()



