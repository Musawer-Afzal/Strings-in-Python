# Write a program to print all the unique combinations of 1,2,3 and 4
# Output:

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# .
# .
# and so on


# Function to generate permutations
def permute(arr, start, end):
    if start == end:
        print(*arr)  # Print the current permutation
    else:
        for i in range(start, end + 1):
            # Swap the elements
            arr[start], arr[i] = arr[i], arr[start]
            # Recursively generate permutations for the next positions
            permute(arr, start + 1, end)
            # Backtrack (undo the swap)
            arr[start], arr[i] = arr[i], arr[start]

# List of numbers
numbers = [1, 2, 3, 4]

# Call the function to generate and print permutations
permute(numbers, 0, len(numbers) - 1)
