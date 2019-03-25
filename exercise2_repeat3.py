sentence = "This is my third attempt to solve something really really simple and I am still getting stuck"

# declaring an empty dictionary
char_counts = {}

for letter in sentence:
    if letter != ' ':
        if letter in char_counts:
            char_counts[letter] += 1
        else:
            char_counts[letter] = 1

# print(char_counts)

# Now sort them
# You cannot sort dictionary
# Convery to list of tuples
char_count_sorted = sorted(
    char_counts.items(), key=lambda kv: kv[1], reverse=True)

print(char_count_sorted[0])
