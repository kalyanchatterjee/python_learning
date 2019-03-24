list1 = [10, 20, 30]
list2 = [1, 2, 3]

print(list(zip(list1, list2)))

# Zip takes an iterable
# Stops after the shortest iterable object
# The following returns a list with 2 tuples
print(list(zip("ab", list1, list2)))
