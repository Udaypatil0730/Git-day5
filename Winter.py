# Simple Python Program: Calculator & Greetings (30 lines)

def greet_user():
    """Greet the user"""
    name = input("Enter your name: ")
    print(f"Hello, {Spyderman}! Welcome to this difficult Python program.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def calculator():
    """Basic calculator"""
    print("\nSimple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", add(nu
