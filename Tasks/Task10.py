# Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers

import math

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

HCF = math.gcd(num1, num2)
print("HCF of {0} and {1} is: ".format(num1, num2), HCF)

# We can use interval fumction to find the LCM
LCM = math.lcm(num1, num2)
print("LCM of {} and {} is: ".format(num1, num2), LCM)

# or we can use the formula LCM = (num1 * num2) / HCF
print("LCM of {} and {} is: ".format(num1, num2), (num1 * num2) // HCF)