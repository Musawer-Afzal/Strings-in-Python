# Write a Python Program to Find the Sum of the Series till the nth term:
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user


n = int(input("Enter n: "))
x = int(input("Enter x: "))
sum = 0

for i in range(1, n+1):
    if sum == 0:
        sum += 1
    else:
        sum += x**i/i

print("Sum of the series: ", int(sum))