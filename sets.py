numbers = [1, 2, 3, 4, 3, 6]

first = set(numbers)
second = {1, 5}

# Union
print(first | second)
# Intersection
print(first & second)
# Difference
print(first - second)
# Symmetric difference - removes elements which are common to both sets
print(first ^ second)

# Check if an element is in a set
if 6 in first | second:
    print("Yes")
else:
    print("No")
