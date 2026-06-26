class InsufficientBalanceError(Exception):
    pass

balance = 5000

try:
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        raise ValueError("Amount must be positive")
    
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    
    print(f"balance before withdrawal: {balance}")
    
    balance -= amount

    print("withdrawal successful.")
    print(f"Remaining balance: {balance}")

except ValueError as e:
    print(f"Invalid input: {e}")

except InsufficientBalanceError as e:
    print(f"Transaction failed: {e}")

finally:
    print("Transaction processed")

    

