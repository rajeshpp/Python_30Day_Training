correct_password = "admin123"
i = 0

while i < 3:
    i += 1
    
    password = input("Enter Password: ")

    if password == correct_password:
        print("Login Successful")
        break

    print("Wrong Password")
else:
    print("Account Blocked")