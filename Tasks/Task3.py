# Write a program to pring the following pattern
#     *
#   * * *
# * * * * *
for i in range(0, 3):
    # Print spaces before the stars
    print('  ' * (3 - i - 1), end='')
        
    # Print stars with space in between
    print('* ' * (2 * i + 1))