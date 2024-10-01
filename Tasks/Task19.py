# Word location in String.
# Statement: Find a location of a word in a given sentence.

# Example 1:
# Input:
# Sentence: We can learn data science through campusx mentorship program.
# word: campusx

# Output:
# Location of the word is 7.



sentence = "We can learn data science through campusx mentorship program."
word = input("Enter a word: ")

sentence = sentence.split()

for i in range(len(sentence)):
    if sentence[i] == word:
        print("Location of the word is ", i + 1)