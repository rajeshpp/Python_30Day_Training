def calculate_interest(amount, rate=10): # Default Arguments MUST always follow non-default arguments
    return amount * rate / 100

# Example usage:
interest1 = calculate_interest(1000, 5)  # Returns 50.0
interest2 = calculate_interest(1000)     # Returns 100.0 (uses default rate of 10)

print(f"Interest with custom rate: {interest1}")  # Output: Interest with custom rate: 50.0
print(f"Interest with default rate: {interest2}")  # Output: Interest with default