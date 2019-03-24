point = {'x': 1, 'y': 2}
# Better way (using keyword arguments):
point = dict(x=1, y=2)

print(point['x'])
point["x"] = 10

if "a" in point:
    print(point['a'])
else:
    print("Not found")

# Alternatively
print(point.get("x", 0))
print(point.get("a", 0))

del point['x']
print(point)

# Add to list
point["z"] = 12

# Iterating over dictionary - Method 1
for key in point:
    print(key, point[key])

# Iterating over dictionary - Method 2
for i in point.items():
    print(i)

# Also - unpacking
for key, value in point.items():
    print(key, value)
