for x in "Python":
    print(x + "\n")  # \n just adds an extra white line in between; aesthetics only

for x in ['a', 'b', 'c']:
    print(x)

for w in range(4, 10):
    print(w)
# step
for w in range(0, 10, 2):
    print(w)
# range doesn't return a list, it returns a range object
print(type(range(5)))


names = ["Jimmy", "Jihn"]

for name in names:
    if name.startswith("Jo"):
        print("Found")
        break
else:
    print("Not found")
# In the above, if you put the else block in the same level as the
# if, then it will print "Not found" for each element it checks.
# Putting else as the same level as for, prints "Not found" only once.
