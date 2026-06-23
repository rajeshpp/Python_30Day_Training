print("Elif Statement Syntax")

print('''
if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    statement4
''')

print("="*50)
print("Examples")
print("="*50)

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")