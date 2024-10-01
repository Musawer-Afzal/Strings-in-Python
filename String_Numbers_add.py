number = int(input("Enter a three digit number: "))

# 345%10 = 5
a = number % 10
number = number // 10

# 34%10 = 4
b = number % 10
number = number // 10

c = number

print(a + b + c)