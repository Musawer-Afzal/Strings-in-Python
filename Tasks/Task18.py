# Find uncommon words from two Strings.
# Statement: Given two sentences as strings A and B. The task is to return a list of all uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.

# Example 1
# Input:
# A = "apple banana mango" 
# B = "banana fruits mango"

# Output:
# ['apple', 'fruits']



A = "apple banana mango"
B = "banana fruits mango"

A = A.split()
B = B.split()

uncommon_words = []

for i in A:
    if i in B:
        continue
    else:
        uncommon_words.append(i)

for i in B:
    if i in A:
        continue
    else:
        uncommon_words.append(i)

print("Uncommon words are: ", uncommon_words)



# OR a more efficient way will be

from collections import Counter

def find_uncommon_words(A, B):
    # Split both strings into lists of words
    words_A = A.split()
    words_B = B.split()

    # Combine the lists and count word occurrences using Counter
    word_count = Counter(words_A + words_B)

    # Find uncommon words (appear exactly once)
    uncommon_words = [word for word in word_count if word_count[word] == 1]

    return uncommon_words

# Example usage
A = "apple banana mango"
B = "banana fruits mango"
result = find_uncommon_words(A, B)
print(result)