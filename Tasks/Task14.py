# Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
# Input:
# hel123O4every093

# Output:
# Sum: 22
# Avg: 2.75




string = str(input("Enter a AlphaNumeric string: "))
sum = 0

for i in string:
    if i.isdigit():
        sum = sum + int(i)
    else:
        continue    

print("Sum of the digits in AlphaNumeric String is: ", sum)