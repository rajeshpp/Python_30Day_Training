def test(x=[]):
    x.append(1)
    return x

print(test())  # Output: [1]
print(test())  # Output: [1, 1]
print(test())  # Output: [1, 1, 1]
