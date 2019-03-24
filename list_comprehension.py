orders = [
    ("Product1", 18),
    ("Product2", 4),
    ("Product3", 22),
]

result = [order[1] for order in orders]

print(result)

# You can also filter it
filtered = [order for order in orders if order[1] >= 10]
print(filtered)
