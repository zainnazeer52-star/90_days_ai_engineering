# Create a program that tracks your AI learning progress.

profile = {
    "name": "Zain",
    "goal": "AI Engineer",
    "skills": [
        "Python",
        "Machine Learning"
    ],
    "completed_days": 5
}


def add_skill():
    new_skill = input("Enter the new skill: ").strip()

    if new_skill == "":
        print("Skill name cannot be empty.")

    elif new_skill in profile["skills"]:
        print("This skill already exists.")

    else:
        profile["skills"].append(new_skill)
        print(f"{new_skill} added successfully.")


def remove_skill():
    skill_name = input("Enter the skill you want to remove: ").strip()

    if skill_name in profile["skills"]:
        profile["skills"].remove(skill_name)
        print(f"{skill_name} removed successfully.")

    else:
        print("Skill not found.")


def show_profile():
    print("\nAI Learning Profile")
    print(f"Name: {profile['name']}")
    print(f"Goal: {profile['goal']}")

    print("\nSkills:")

    if len(profile["skills"]) == 0:
        print("No skills added.")

    else:
        for number, skill in enumerate(profile["skills"], start=1):
            print(f"{number}. {skill}")

    print(f"\nCompleted Days: {profile['completed_days']}")


def update_completed_days():
    try:
        new_days = int(input("Enter completed learning days: "))

        if new_days < 0:
            print("Completed days cannot be negative.")

        else:
            profile["completed_days"] = new_days
            print("Completed days updated successfully.")

    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    while True:
        print("\nAI Skill Tracker")
        print("1. Add New Skill")
        print("2. Remove Skill")
        print("3. Show Profile")
        print("4. Update Completed Days")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_skill()

        elif choice == "2":
            remove_skill()

        elif choice == "3":
            show_profile()

        elif choice == "4":
            update_completed_days()

        elif choice == "5":
            print("AI Skill Tracker closed.")
            break

        else:
            print("Invalid option. Please select 1 to 5.")


show_menu()
