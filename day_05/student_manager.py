# STUDENT MANAGMENT SYSTEM
# Build a program that stores students.

# Features:

# Add student
# View students
# Search student
# Exit

students = []


def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\nStudent List:")

    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")


def search_student():
    search_name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            return

    print("Student not found.")


while True:

    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank you for using Student Management System")
        break

    else:
        print("Invalid choice. Try again.")
