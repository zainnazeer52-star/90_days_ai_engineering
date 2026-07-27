# Use a function with variable-length arguments to calculate total marks for any number of students.

def total_scores(*scores):
    return sum(scores)


print(total_scores(80, 90, 70, 85))
