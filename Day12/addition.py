def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3))
print(add(5, 10, 15, 20))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 9 ,4, 5, 6))