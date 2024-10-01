# Reverse words in a given String
# Statement: We are given a string and we need to reverse words of a given string.

# Example 1:
# Input:
# geeks quiz practice code

# Output:
# code practice quiz geeks

str = str(input("Enter a string: "))
str = str.split()
str.reverse()
print(" ".join(str))