#Question 1: Temp. Converter App
from unittest import result

temp = float(input("Enter the temperature: "))
unit = input ("Is the temperature in C or in F? ").upper()

if unit == "F":
    celsius = (temp - 32) * 5 / 9
    print("Temperature in Celsius: ", celsius)

elif unit == "C":
    fahrenheit = (temp * 9 / 5) + 32
    print("Temperature in Fahrenheit: ", fahrenheit)

else:
    print("Invalid input...Please enter either F or C.")

