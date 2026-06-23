user_input_username = input("Enter your username: ") # UI
user_input_password = input("Enter your password: ") # UI

stored_username, stored_password = "admin", "python123" # DB

if user_input_username == stored_username and user_input_password == stored_password:
    print("Login successful!")
else:
    print("Invalid username or password.")