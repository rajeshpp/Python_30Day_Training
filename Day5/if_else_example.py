print("If-Else Statement Syntax")
print('''
if condition:
    statement 1
else:
    statement 2
''')

print("="*50)
print("Examples")

# Examples
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult & eligible to vote.")
else:
    print("You are a minor & not eligible to vote.")    

print("="*50)

temperature = int(input("Enter the temperature: "))

if temperature > 25:
    print("It's a hot day. Stay hydrated!")
else:
    print("It's not a hot day.")