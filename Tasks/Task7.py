# Find the sum of the series upto n terms.
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. 
# Take the user input and then calculate. And the output style should match which is given in the example.
# Example 1:

# Input:
# 5

# Output:
# 2+22+222+2222+22222
# Sum of above series is: 24690

n = int(input("Enter n: "))
value = int(input("Enter x: "))
current_term = 0
sum = 0
series_terms = []

for i in range(1, n+1):
    current_term = current_term * 10 + value
    series_terms.append(str(current_term))
    sum += current_term

print("+".join(series_terms))
print("Sum of above series is: ", sum)