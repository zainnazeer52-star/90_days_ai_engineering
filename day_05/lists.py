# Lists in Python

skills = ["Python", "Machine Learning", "Deep Learning"]

print(skills)
print(skills[0])
print(skills[1])

skills.append("Generative AI")
print(skills)

skills.remove("Deep Learning")
print(skills)

print(len(skills))

# PRACTICE

projects = [
    "Calculator",
    "Password Checker",
    "AI Profile Generator"
]

for project in projects:
    print(project)

# LIST SLICING: access multiple items.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0:5])
print(numbers[2:6])
print(numbers[-5:-2])
print(numbers[:-2])
