def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

a, b = map(int, input("Enter two numbers separated by space: ").split())
print("Choose an operation: add, subtract, multiply, divide")
operation = input("Enter the operation: ").strip().lower()
result = calculator(a, b, operation)
if isinstance(result, str):
    print(result)
else:
    print(f"The result of {operation} between {a} and {b} is: {result}")