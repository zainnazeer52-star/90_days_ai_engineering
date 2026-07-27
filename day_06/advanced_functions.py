def great_user(name="User", role="AI Learner"):
    print(f"Hello {name}, Welcome to the {role} learning Program!")


great_user()
great_user("Zain")
great_user(role="Python Developer")
great_user("Umer", "AI Engineer")

# VARIABLE LENGTH ARGUMENTS


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add_numbers(10, 20, 30))


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Zain", role="AI Engineer", city="Lahore")
