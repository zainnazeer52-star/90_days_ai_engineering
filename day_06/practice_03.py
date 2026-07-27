# Create a lambda function to filter scores above 80 from a list.

scores = [80, 90, 70, 85, 60]
above_80 = list(filter(lambda x: x > 80, scores))
print(above_80)
