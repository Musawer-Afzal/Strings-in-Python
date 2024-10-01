# Append second string in the middle of first string
# Input:
# campusx
# data

# Output:
# camdatapusx


str1 = str(input("Enter first string: "))
str2 = str(input("Enter second string: "))

print(len(str1))
# To find the length of the string
mid_str1 = len(str1) // 2

result = str1[:mid_str1] + str2 + str1[mid_str1:]
print(result)