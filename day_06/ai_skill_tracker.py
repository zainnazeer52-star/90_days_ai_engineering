profile = {
    "name": "Zain",
    "goal": "AI Engineer",
    "skills": ["Python", "Machine Learning"],
    "completed_days": 5
}

with open("ai_profile.txt", "w") as file:
    for key, value in profile.items():
        file.write(f"{key}:{value}\n")

with open("ai_profile.txt", "r") as file:
    for line in file:
        print(line.strip())
