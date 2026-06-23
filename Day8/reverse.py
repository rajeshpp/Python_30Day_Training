value = input("Enter a String: ")

empty = ""
for i in range(len(value)-1, -1, -1):
    empty += value[i]

print(empty)

print(value)
print(value[::-1])