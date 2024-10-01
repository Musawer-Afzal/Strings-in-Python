# Strings are a sequence of Unicode Characters

# Create Strings
str1 = "Hello"
str2 = 'World'
str3 = '''Hi'''
str4 = """Hello World"""
print(str1, str2, str3, str4)


# Accessing Substrings from a String
# Indexing
str = "Hello World"
print(str[0], str[6])

# Negative Index
# Last character is assigned to -1
# Second last character: -2
# And so on
str = "Hello World"
print(str[-1])



# Slicing
str = "Hello World"
print(str[0:5])

# To go from one number till the end
print(str[2:])

# Skip every Number
print(str[:])

# To Skip on particular intervals
#        start:stop:step/skip
print(str[ 0 :   7 :  2 ])

# Skip in Reverse
#        Larger -> Small: Step/Skip
print(str[ 6   :     0   :   -1]) # To skip in Reverse You need to move from larger to smaller number


# Print a String in Ascending Order
print(str[::])


# Print a Sring in Reverse
print(str[::-1])
print(str[::-2]) # To Skip 2 Characters at a time


# Print a String Using Negative Value
print(str[-5:]) # It will start from "W" and go till the end
print(str[-5:-1]) # It will start from "W" and go till "l"

# Print in Reverse Using Negative Value
print(str[-1:-6:-1]) # It will start from "l" and go till "W"




# Editing and Deleting in Strings
# Python Strings are Immutable, mean they cannot be changed/ Edited unlike C++
# Example

str = "Hello World"
# s[0] = "h" # This will throw an error

# Delete
str = "Hello World"
del str # It will throw an error

# Question
str = "Hello World"
# It will throw an Error since we are trying to change the string using slicing
# which is not allowed in Python
# del str[-1: -6: -2] 


# String Concatenation
str1 = "Hello\n" # \n is used to create a new line every time "Hello" is Printed
str2 = "World"
print(str1 + " " + str2)

# String Multiplication
print(str1 * 3)

                 # ****************************************

# Arithmetic Operations
# Equal to 
"Peshawar" == "Karachi" # False
# Not Equal to
"Peshawar" != "Karachi" # True



# Lexigraphically Comparison
# The Strings being compared are checked in a dictionary order
# and since Peshawar comes after Karachi in a Dictionary, it states False
# Greater than
"Peshawar" > "Karachi" # False
# Less than
"Peshawar" < "Karachi" # True
# Greater than or Equal to
"Peshawar" >= "Karachi" # False
# Less than or Equal to
"Peshawar" <= "Karachi" # True
# If values are same
# It will be False since the ASCII Value of Capital "P" is less than "p"
"Peshawar" > "peshawar" # False



# Logical Operators
# In Python if the string have a value then it is considered True else False
# And
# The And Operator returns True if both the operands are True
# It checked the First String which was True bit since it has AND operation
# it checked the Second String which was also True and it returns True, which
# was the Second String because it was the last string it checked
print("Hello" and "World")

# OR
# In OR Operation if only one string is true than the result will be true
# Hello will be printed since it will only check the First String and Print True
# which will be the value of First String 
print("Hello" or "World")

# Not
# Since Empty String is False it will return True and Vice Versa
print(not "")



# Loops in Strings
# Print a string
for i in "hello":
    print(i)

# The Loop will run for the number of characters in Peshawar i.e: 8
for i in "Peshawar":
    print("Karachi")



# Membership Operators
# This is case Sensitive
print('P' in 'Peshawar') # It will return True
print('p' in 'Peshawar') # It will return False

                  # **************************************


                             # STRING FUNCTIONS. len, max, min, sorted

# Length of String
print(len("Hello World")) # It will return the length of the String

# Maximum of String
print(max("Hello World")) # It will return the maximum character of the String According to ASCII

# Minimum of String
print(min("Hello World")) # It will return the minimum character of the String According to ASCII

# Sorted in String in Ascending Order
print(sorted("Hello World")) # It will sort the String in Ascending Order

# Sorted in String in Descending Order
print(sorted("Hello World", reverse = True)) # It will sort the String in Descending Order



                     # ****************************************

                     # Capitalize/Title/Upper/Lower/Swapcase


# Capitalize
s = 'hello world'
print(s.capitalize())

# Title
# Capiitalize first letter of each word
s = 'hello world'
print(s.title())

# Upper
# It will convert all characters to Upper Case
s = 'hello world'
print(s.upper())

# Lower
# It will convert all characters to Lower Case
s = 'Hello world'
print(s.lower())

# Swapcase
# It will convert all characters in Upper Case to Lower Case and vise versa
s = "HeLlo WoRLd"
print(s.swapcase())



                        # ************************************

                        # COUNT/FIND/INDEX/STARTSWITH/ENDSWITH

# Count
# It will return the number of times l appears in the String
s = 'hello world'
print(s.count('l'))

# Find
# It will return the index of the first occurence of 'l' or a word in the String
s = 'hello world'
print(s.find('l'))
# This will return -1 since 'x' is not in the String
print(s.find("x"))

# Index
# It will return the index of the first occurence of 'l' or a word in the String
s = 'hello world'
print(s.index('l'))
# This will generate an error since 'x' is not in the String
# print(s.index("x"))

# Startswith
# It will return True if the String starts with 'h'
s = 'Hello World'
print(s.startswith('h')) # Will give True

# Endswith
# It will return True if the String ends with 'd'
s = 'Hello World'
print(s.endswith('d')) # Will give True 
print(s.endswith('s')) # Will give False


                       # ************************************

# Format
# To put a value in a String we use {}
name = "John"
gender = "male"
print("Hi, my Name is {} and i'm a {}".format(name,gender))
# Index can be used to specify a certain value position
print("Hi, my Name is {1} and i'm a {0}".format(gender, name))



                         # **************************************

                         # isalnum/isalpha/isdigit/islower/isidentofier/split/join

# isalnum
# It will return True if all characters in the String are alphanumeric
s = "Hello123"
print(s.isalnum()) # Will give True

# isalpha
# It will return True if all characters in the String are alphabetic
s = "Hello"
print(s.isalpha()) # Will give True

# isdigit
# It will return True if all characters in the String are digits
s = "123"
print(s.isdigit()) # Will give True 

# isidentifier
# It will return True if the String is a valid identifier
s = "hello"
print(s.isidentifier()) # Will give True
s = "hello-123"
print(s.isidentifier()) # Will give False

# split
# It will split the String into a list of words
s ="Hello, Welcome to Programming"
print(s.split()) # Will give ['Hello,', 'Welcome', 'to', 'Programming'] as a list
print(s.split('l')) # Will give ['He', 'o, Wel', 'come to Programming'] as a list

# join
# It will join the list of words into a String
s = ['Hello', 'Welcome', 'to', 'Programming']
print(' '.join(s)) # Will give Hello Welcome to Programming as a String 
print("_".join(s)) # Will give Hello Welcome to Programming as a String joined by "_"

# Replace
s = "Hi, welcome to programming"
print(s.replace('Hi', 'Hello')) # Will give Hello, welcome to programmings

# Strip
# Remove all useless whitespaces from the String
s = "  Hello World  "
print(s.strip()) # Will give "Hello World" as a String