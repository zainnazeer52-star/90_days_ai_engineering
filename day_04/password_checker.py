# Create a function that checks:
# Password length
# Contains numbers
# Contains uppercase letters

def check_password_strength(password):
    has_numbers = False
    has_uppercase = False

    for char in password:
        if char.isdigit():
            has_numbers = True

        if char.isupper():
            has_uppercase = True

    if len(password) >= 8 and has_numbers and has_uppercase:
        return "Strong"
    else:
        return "week"


password = input("Enter you password here: ")
strength = check_password_strength(password)

print(f"password strength: {strength}")
