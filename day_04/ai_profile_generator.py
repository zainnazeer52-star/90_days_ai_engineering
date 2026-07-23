# Build a function based profile generator.

def create_profile(name, skill, language, goal):

    profile = (
        f"Name: {name}\n"
        f"Skill: {skill}\n"
        f"Language: {language}\n"
        f"Goal: {goal}"
    )

    return profile


name = input("Enter your name here: ")
skill = input("Enter you skill level: ")
language = input("Enter you programing language: ")
goal = input("Enter your goal here: ")

print(create_profile(name, skill, language, goal))
