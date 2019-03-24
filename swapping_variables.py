x = 10
y = 11

print("x id:", id(x))
print("y id:", id(y))
# How can you swap the two without adding a new variable
x = x + y
print("x id:", id(x))
print("y id:", id(y))
y = x - y
print("x id:", id(x))
print("y id:", id(y))
x = x - y
print("x id:", id(x))
print("y id:", id(y))

# Using Python
x, y = y, x
print(x)
print(y)
