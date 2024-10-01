# The natural logarithm can be approximated by the following series.
# (x-1/x) + 1/2(x-1/x)^2 + 1/2(x-1/x)^3 + 1/2(x-1/x)^4 + ...... +  1/2(x-1/x)^n

# If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.


n = int(input("Enter n: "))
x = int(input("Enter x: "))

sum = 0

for i in range(1, n+1):
    if sum == 0:
        sum += (x - 1) / x
    else:
        sum += 1/2 * ((x - 1) / x)**i

print("Sum of the series: ", sum)