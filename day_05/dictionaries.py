developer = {
    "name": "Zain",
    "role": "AI Engineer",
    "language": "Python"
}


print(developer)

print(developer["name"])
print(developer["role"])

# UPDATE DICTIONARY DATA
developer["experience"] = "Intermediate"
developer["age"] = 22

print(developer)

# REMOVE DATA
del developer["age"]
print(developer)
