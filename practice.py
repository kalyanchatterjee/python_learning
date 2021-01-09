numbers = range(20)

print(id(numbers))

print(numbers)
print(list(numbers))

numbers = list(numbers)
print(id(numbers))
print(numbers[:])
print(numbers[0:20])
print(numbers[::3])
numbers.append(20)
# In Python a list is mutable. The following doesn't create a new list.
print(id(numbers))

# Print numbers in reverse
print(numbers[::-1])
print(numbers[::-2])

# List unpacking
first, second, third = [1, 2, 4]
print(first)
print(second)
print(third)
first, *others = [1, 2, 4]
print(first)
print(others)

# Looping through a list
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number)
# If you want to find the index
for index, number in enumerate(numbers):
    print(index, ",", number)

# add item to the list
numbers.append(7)
numbers.insert(0, 0)
print(numbers)

# [0, 1, 2, 3, 4, 5, 6, 7]
# remove from list
numbers.pop()
print(numbers)
numbers.pop(2)
print(numbers)
# delete a range of numbers
del numbers[0:2]
print(numbers)
