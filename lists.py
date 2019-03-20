my_list = ['apple', 'orange', 'banana']
print(id(my_list))
# adding to the list
print(id(my_list.append('watermelon')))


my_list2 = my_list

print(my_list == my_list2)

print(my_list)
print(my_list2)

text = "abcd"
print(len(text))

# Repeat items in a list
my_list3 = ['a']
print(my_list3 * 100)

# Using a range
my_list4 = list(range(10))
print(my_list4)

chars = list("Hello world")
print(chars)

# length of a list
print(len(chars))


# List methods
letter = ['a', 'b', 'c', 'd']
print(letter[0])
print(letter[-1])
print(letter[0:3])

# Print every other item in the list
numbers = list(range(20))
print(numbers[::2])
# print numbers in reverse order
print(numbers[::-1])


# List unpacking
first, second, third, *other = numbers
print(first)
print(other)
first, *other, last = numbers
print(other)


# enumeration, returns a tuple -> (index, element)
letters = ['a', 'b', 'c']
for letter in enumerate(letters):
    print(letter[0], letter[1])
# We can also obtain the index with unpacking
for index, letter in enumerate(letters):
    print(index, letter)

# Add
letters.append('d')

# Insert
letters.insert(len(letters), "-")

# Remove
letters.pop()

# Remove item at given index
letters.pop(0)

# Remove item by providing its value
letters.remove("b")

print(letters)

letters.append('e')
letters.append('f')
letters.append('g')

print(letters)

del letters[0:2]

print(letters)

# Delete the contents of the list
letters.clear()

# Finding elements in a list
if "d" in letters:
    print(letters.index("d"))
else:
    print("Item not found")

# Sorting
letters = ['a', 'd', 'b', 'e', 'c']
letters.sort()
print(letters)
letters.sort(reverse=True)
print(letters)
numbers = [9, 6, 5, 51, 12, 4]
print(id(numbers))
# Unlike sort, sorted doesn't modify the original list
print(id(sorted(numbers)))
