from utils import *


# celsius_value = input("enter a value for celsius: ")
# celsius_value = float(celsius_value)


def conversion(celsius: float):
    fahrenheit = multiplication(celsius, 1.8)
    new_fahrenheit = addition(fahrenheit, 32)
    return new_fahrenheit


#
# print(conversion(celsius_value))

celsius_value = input("enter values separated by commas ")
celsius_values = celsius_value.split(",")
print(celsius_values)

for temperatures in celsius_values:
    converted = conversion(float(temperatures))
    print(f"the value of {temperatures} in fahrenheit is {converted}")
