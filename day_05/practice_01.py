# Create a list of your top 5 AI skills.

# Requirements:

# Add one new skill
# Remove one skill
# Print all skills using a loop

skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "FastAPI",
    "Git"
]

skills.append("Deep Learning")
print(skills)

skills.remove("SQL")
print(skills)

for skill in skills:
    print(skill)
