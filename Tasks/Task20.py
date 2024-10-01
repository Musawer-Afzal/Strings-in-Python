# Write a program that can remove all the duplicate characters from a string. User will provide the input.



input_string = input("Enter a string: ")
result = ""

for char in input_string:
    if char not in result:
        result += char

print(result)