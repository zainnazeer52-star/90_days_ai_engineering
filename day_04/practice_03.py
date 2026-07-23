# Create a function to calculate the area of a rectangle.

def calculate_area(width, length):
    return width * length


print("Total Area:", calculate_area(2, 3))

# Create a function that converts Celsius to Fahrenheit.


def temperature_converter(temp_celcius):
    F = temp_celcius * 9/5 + 32
    return F


result = temperature_converter(25)

print(result)
