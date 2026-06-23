expenses = []
how_many_days = int(input("How many days of expenses do you want to track? "))

for day in range(1, how_many_days + 1):
    expense = float(input(f"Enter expenses for day {day}: "))
    expenses.append(expense)

print("\nDaily Expenses:")
for day, expense in enumerate(expenses, start=1):
    print(f"Day {day}: ${expense:.2f}")

print(f"\nTotal Expenses: ${sum(expenses):.2f}")