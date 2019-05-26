sentence = "this is a sentence where you need to find the most repeated letter"

# get all the unique letters
letters = set(sentence)

# Declare a dictionary object to store the results
letterCounts = dict()

# Now go through the string and get a count for each letter in the string
for letter in letters:
    if letter != ' ':
        letterCount = len(list(filter(lambda x: x == letter, sentence)))
        letterCounts[letter] = letterCount

# How to sort? Dictionary is unordered
x = letterCounts.items()
print(x)
print("sorted:")
print(sorted(x, key=lambda kv: kv[1], reverse=True)[0])
