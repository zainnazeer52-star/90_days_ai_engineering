# Multiply two numbers
def multiply(x, y): return x * y


print(multiply(5, 3))


def square(x): return x ** 2


print(square(7))

students = [("Ali", 25), ("Zain", 22), ("Sara", 24)]
students.sort(key=lambda x: x[1])
print(students)
