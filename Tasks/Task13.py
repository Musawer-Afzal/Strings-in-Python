# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of 
# a string so that all lowercase letters should come first.
# Given:
# str1 = PyNaTive

# Expected Output:
# yaivePNT



str1 = "PyNaTive"

lenght_str1 = len(str1)
for i in range(0, lenght_str1):
    if str1[i].islower():
        print(str1[i], end = "")
    else:
        continue

for i in range(0, lenght_str1):
    if str1[i].isupper():
        print(str1[i], end = "")
    else:
        continue