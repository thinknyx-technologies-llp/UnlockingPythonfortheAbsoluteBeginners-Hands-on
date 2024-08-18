correct_password = 'password123'
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Access granted.")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Incorrect password, please try again.")
        else:
            print("Too many unsuccessful attempts. You are blocked.")