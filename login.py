def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Invalid username or password")

# Call the login function
login()