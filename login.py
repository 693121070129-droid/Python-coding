user = {"username": "raika", "password": "8520"} #right username and password
username = input("Enter your username: ")# input username
password = input("Enter your password: ")# input password
for attempt in range(3): # allow 3 attempts
    if username == user["username"] and password == str(user["password"]):
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
else:
    print("Too many failed attempts. Please try again later.")