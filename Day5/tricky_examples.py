# print("What is the difference between = & ==")

a = 1

if a:
    print("a is truthy")
else:
    print("a is falsy")

"""
Values Considered as Falsy:

False
0
0.0
''
""
[]
{}
()
None
"""

x = 79

if x > 50:
    print("A")
elif x > 75:
    print("B")

if x > 50:
    print("A")    
if x > 75:
    print("B")

if 10 > 5 > 2:
    print("True")