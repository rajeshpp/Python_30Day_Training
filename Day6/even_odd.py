value = int(input("Emter a Number: "))

for val in range(1, value+1):
    if val % 2 == 0:
        print(f"{val} is even number")
    else:
        print(f"{val} is odd number")