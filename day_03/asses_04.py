password = "abcd4321"
attempts = 3

while attempts > 0:
    try_password = input("Please enter your password here: ")

    if try_password == password:
        print("Your password matches.")
        break

    attempts = attempts - 1
    print("Your password is incorrect.")
    print(f"You have {attempts} attempts left.")

else:
    print("You have 0 attempts left.")
    print("Access denied.")
