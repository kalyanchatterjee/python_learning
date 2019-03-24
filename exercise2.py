sentence = "This is a common interview question"
# Find the most repeated character in the sentence above

charSet = set(sentence)
letterCounts = dict()
for letter in charSet:
    # Save in a dictionary
    if letter != ' ':
        letterCount = len(list(filter(lambda x: x == letter, sentence)))
        letterCounts[letter] = letterCount

print(letterCounts)
