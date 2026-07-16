# Learn Logical Operators

# AND OPERATOR

age = int(input("Enter your age: "))
has_an_card = input("Do you have an ID card? Enter yes or no: ")

if age >= 18 and has_an_card.lower() == "yes":
    print("you are eligible. ")

else:
    print("you are not eligible ")

# OR OPERATOR

day = input("Enter the day: ")

if day == "saturday" or day == "sunday":
    print("it's a weekend. ")
else:
    print("it is a working day. ")

# NOT OPERATOR

is_logged_in = False

if not is_logged_in:
    print("Please log in. ")
