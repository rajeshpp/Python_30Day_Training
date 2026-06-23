correct_pin = "1234"

for attempt in range(3):
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Login Successful")
        break

    print("Wrong PIN")

else:
    print("Account Blocked")