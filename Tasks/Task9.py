# Write a program that will take a decimal number as input and prints out the binary equivalent of the number

num = int(input("Enter a decimal number: "))
binary_values = []

# print(bin(num))

while num > 1:
    bit_value = num % 2
    binary_values.append(bit_value)
    num = num // 2

binary_values.append(num)
binary_values.reverse()
print("Binary value:", ''.join(map(str, binary_values)))