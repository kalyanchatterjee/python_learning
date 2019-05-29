x = 34
y = 32


def f():
    global x, y
    x = 38
    y = 83


print(x)
print(y)
f()
print(x)
print(y)
