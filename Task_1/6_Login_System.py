# Login System

stored_username = "admin"
stored_password = "1234"

max_attempts = 3

for attempt in range(max_attempts):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == stored_username and password == stored_password:
        print("Login successful!")
        break
    else:
        remaining = max_attempts - (attempt + 1)

        if remaining > 0:
            print("Invalid username or password.")
            print("Remaining attempts:", remaining)
        else:
            print("Invalid username or password.")
            print("Account locked.")


