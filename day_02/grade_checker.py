# Day 2 Mini Project Student Grade Checker

student_name = input("Enter the student name: ")
marks = float(input("Enter marks out of 100: "))

if marks < 0 and marks > 100:
    print("invalid marks: Please enter a value between 0 and 100. ")
elif marks > 95:
    grade = "A Plus"
elif marks > 90:
    grade = "A "
elif marks > 80:
    grade = "B Plus "
elif marks > 70:
    grade = "B "
elif marks > 60:
    grade = "C "
elif marks > 50:
    grade = "D "
else:
    print("Fail. ")

print()
print("Student Result. ")
print(f"Student name: {student_name}")
print(f"Student Marks: {marks}")
print(f"Student Grade: {grade}")
