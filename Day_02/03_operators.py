# Modulus -> displays the remainder
# print(9 % 2)
# # Exponentiation -> to the power of
# print(2**3)
# Floor Division -> divide then take away decimal
# print(7 // 2)
# f_degrees = input("Please provide your Farenheit: ")
# print(f"The {f_degrees} is {int(f_degrees) * 0.56}")

# Task 2

# b_year = int(input("Please provide your birth year: "))
# print(f"Your age is {2025 - b_year}")

# Task 3

pi = 3.14
rad = float(input("Provide radius of circle "))
print(f"Area of circle is {pi * rad**2}")

# Task 4

import math

val = int(input("Enter a value: "))
load = math.floor(val / 10)
print(f"[{load * '=' + (10 - load) * ' '}]")
