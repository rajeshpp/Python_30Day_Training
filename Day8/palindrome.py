value = input("Enter a value: ")

# Basic version using if-else statement
if value == value[::-1]:
    print("The value is a palindrome")
else:
    print("The value is not a palindrome")

# Simplified version using ternary operator
outcome = "This is a palindrome" if value == value[::-1] else "This is not a palindrome"
print(outcome)