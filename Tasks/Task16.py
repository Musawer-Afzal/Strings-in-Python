# Check whether the string is Symmetrical.
# Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical 
# if both the halves of the string are the same.

# Example 1:
# Input
# khokho

# Output
# The entered string is symmetrical


str = str(input("Enter a string: "))

mid = len(str) // 2

if (str[:mid] == str[mid:]):
    print("The entered string is symmetrical")
else:
    print("Not symmetrical")