def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
         return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return False
    print(f"{num} is a prime number.")
    return True

print(is_prime(int(input("Enter a number to check if it's prime: "))))