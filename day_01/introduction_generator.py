# name = input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")
# career_goal = input("Enter your career goal: ")
# current_role = input("Enter your current role: ")

# print("Person Introduction")
# print("My name is", name)
# print("My age is", age)
# print("My city is", city)
# print("My career goal is", career_goal)
# print("My current role is", current_role)

# now using formatted string

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
career_goal = input("Enter your career goal: ")

introduction = (
    f" My name is {name}. "
    f"I am {age} years old. "
    f"My goal is to become a {career_goal}. "
)

print(introduction)
