# Tuples are ordered but cannot be changed.

numbers = (10, 20, 30, 40, 50)

print(numbers)
print(type(numbers))  # tuple

print(numbers[2])

# tuples through Loops

ai_stack = (
    "Python",
    "PyTorch",
    "FastAPI"
)

for tool in ai_stack:
    print(tool)
