# Simple Login System.

correct_username = "admin"
correct_password = "12345"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")