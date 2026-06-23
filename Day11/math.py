def add(a, b):
    print(f"The sum of {a} and {b} is: {a + b}")

def subtract(a, b):
    print(f"The difference between {a} and {b} is: {a - b}")

def multiply(a, b):
    print(f"The product of {a} and {b} is: {a * b}")

def divide(a, b):
    if b != 0:
        print(f"The quotient of {a} divided by {b} is: {a / b}")
    else:
        print("Error: Division by zero is not allowed.")


m, n = map(int, input("Enter two numbers separated by space: ").split())
add(m, n)
subtract(m, n)
multiply(m, n)
divide(m, n)