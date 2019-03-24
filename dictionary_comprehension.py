values = []
print(id(values))
for x in range(5):
    values.append(x ** 2)
# print(values)
print(id(values))

# More concisely...
values = [x ** 2 for x in range(5)]
# print(values)
print(id(values))

# Replace [] with {}
values = {x ** 2 for x in range(5)}
print(type(values))

# Dictionary comprehension
values = {x: x ** 2 for x in range(5)}
print(values)
