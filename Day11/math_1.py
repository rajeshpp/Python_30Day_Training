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
        raise ValueError("Error: Division by zero is not allowed.")


a, b = map(int, input("Enter two numbers separated by space: ").split())
print(f"The sum of {a} and {b} is: {add(a, b)}")
print(f"The difference between {a} and {b} is: {subtract(a, b)}")
print(f"The product of {a} and {b} is: {multiply(a, b)}")
try:
    print(f"The quotient of {a} divided by {b} is: {divide(a, b)}")
except ValueError as e:
    print(e)