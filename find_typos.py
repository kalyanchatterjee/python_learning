# This is the question I was asked in the Ritual interview

# Given a sentence, how can you find the typos and how can you
# suggest words for those typos

# Downloaded webster dictionary in a JSON format
# Googled "how to read JSON file in Python" - https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

import json

with open('dictionary.json', 'r', encoding="utf-8") as myfile:
    data = myfile.read()

eng_dict = json.loads(data)

sentence = "apple felll fromm the tree"

words = sentence.split(' ')

typo_index = []
word_counter = 0
for word in words:
    word_counter = word_counter + 1
    if word not in eng_dict:
        typo_index.append(word_counter)

# Highlight the typo
marked_sentence = ""
word_counter = 0
for word in words:
    word_counter = word_counter + 1
    if word_counter in typo_index:
        marked_sentence = marked_sentence + " [" + word + "] "
    else:
        marked_sentence = marked_sentence + " " + word

print(marked_sentence)
