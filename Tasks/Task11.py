# Create Short Form from initial character
# Given a string create short form ofthe string from Initial character. Short form should be capitalised.

# Example:
# Input:
# Data science mentorship program

# Output:
# DSMP


random_string = str(input("Enter a Random String: "))
random_string = random_string.split()
length_of_string = len(random_string)
short_form = []

for i in range(0, length_of_string):
    string = random_string[i]
    first_char = string[0]
    short_form.append(first_char.upper())


print("".join(short_form))