# What if we have a list of complex objects
orders = [
    ("Product1", 18),
    ("Product2", 4),
    ("Product3", 22),
]

# def sort_item(item):
#     return item[1]

# # passing a reference to function sort_item
# orders.sort(key=sort_item)
# print(orders)

# The above is ugly U G L Y

# Shorter and cleaner way is to use Lambda function
orders.sort(key=lambda item: item[1])
print(orders)

# Let's say you want to get all the prices
prices = []
for order in orders:
    prices.append(order[1])
print(prices)

# Using a map function
x = map(lambda order: order[1], orders)
print(x)

# x is an object
print(list(x))

y = filter(lambda order: order[1] == 22, orders)
print(list(y))

# See list_comprehension.py for a better implementation
