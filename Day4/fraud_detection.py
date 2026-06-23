transaction_amount = float(input("Enter the transaction amount: "))
account_age = int(input("Enter the account age in years: "))
account_balance = float(input("Enter the account balance: "))

high_transaction_threshold = account_balance * 0.5

transaction_location = "Singapore"
user_location = "Hyderabad"


if transaction_amount > high_transaction_threshold and account_age < 1:
    print("Transaction flagged as potentially fraudulent.")
elif transaction_amount > account_balance and transaction_location != user_location:
    print("Transaction flagged as potentially fraudulent due to location mismatch.")
else:
    print("Transaction is likely legitimate.")