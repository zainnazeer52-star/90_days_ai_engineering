# Ask the user for a username and password.

correct_username = "zain3032"
correct_password = "abcdijk123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login successfully...")
else:
    print("invalid username and password. ")
