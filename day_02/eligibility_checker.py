python_level = input(
    "Enter your Python level, beginner, intermediate, advanced: "). lower()

know_math = input("Do you know about mathemarics? Enter yes or no: ").lower()

study_hours = float(input("Enter your daily study hours: "))

if (
    python_level in ["beginner", "intermediate", "advanced"]
    and know_math == "yes"
    and study_hours >= 2
):
    print("you are ready to continue your AI Engineering journey. ")

elif study_hours < 2:
    print("Try to allocate 2 hours study daily")
else:
    print("Strenght your python and mathematics foundations ")
