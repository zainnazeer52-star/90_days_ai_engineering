dataset = [
    {"name": "Ali", "score": 80},
    {"name": "Ahmed", "score": 90},
    {"name": "Sara", "score": 70}
]


# Total students
total_students = len(dataset)


# Calculate total score
total_score = 0

for student in dataset:
    total_score = total_score + student["score"]


# Average score
average_score = total_score / total_students


# Highest score
highest_score = 0

for student in dataset:
    if student["score"] > highest_score:
        highest_score = student["score"]


# Display result
print("Total students:", total_students)
print("Average score:", average_score)
print("Highest score:", highest_score)
