# Word Frequency Counter 

# Take a paragraph as input and:

# Count frequency of each word
# Ignore punctuation
# Ignore case sensitivity


# 💡 Hint:
# Use string module → string.punctuation
# Consider using a dictionary

import string

text = str(input("Enter Text:").lower())

for s in string.punctuation:
    text = text.replace(s,"")

word = text.split()

freq = {}

for w in word:
    freq[w] = freq.get(w, 0) + 1

for w, count in freq.items():
    print(f"{w} : {count}")
