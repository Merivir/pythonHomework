import random

def custom_add(x, y):
    return x + y

def custom_subtract(x, y):
    return x - y

def custom_multiply(x, y):
    return x * y

def custom_divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def my_secret_calculator():
    while True:
        print("Welcome to the Custom Calculator")
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'exit' to quit")

        user_input = input(": ")

        if user_input == "exit":
            break
        elif user_input in ["add", "subtract", "multiply", "divide"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: ")

            if user_input == "add":
                print("Result: ", custom_add(num1, num2))
            elif user_input == "subtract":
                print("Result: ", custom_subtract(num1, num2))
            elif user_input == "multiply":
                print("Result: ", custom_multiply(num1, num2))
            elif user_input == "divide":
                print("Result: ", custom_divide(num1, num2))
            else:
                print("Invalid input")
        else:
            print("Invalid input")

if __name__ == "__main__":
    my_secret_calculator()
