# Removal of all characters from a string except integers
# Given:

# str1 = 'I am 25 years and 10 months old'
# Expected Output:

# 2510




str1 = 'I am 25 years and 10 months old'
integers = ""

for i in str1:
    if i.isdigit():
        integers = integers + i
    else:
        continue

print(integers)