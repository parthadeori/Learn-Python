# 1. Write a program that calculates the area of a circle. Prompt the user to enter the radius of the circle, and use the math.pi constant to perform the calculation.
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is:", area)


# 2. Create a program that converts degrees to radians. Prompt the user to enter an angle in degrees, and use the math.radians() function to convert it to radians.
import math

degrees = float(input("Enter an angle in degrees: "))
radians = math.radians(degrees)
print("The angle in radians is:", radians)