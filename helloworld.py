# Data types in Python
# Integer
student_count = 1000
age: int = 20
# Linter mypy will flag the following as an error
# age = "Python"
# Float
rating = 4.88
# Boolean
is_published = False
# String
course = "Learning Python with Mosh"
message = """
hello, 

This is a multi-line string. 

That's all
"""

print(message)

# Length of a string using len()
print(len(course))

print(course[0])

print(course[-1])

print(course[0:3])

print(id(course))
course = course + " - Part 1"
# A string is immutable. So when you modify the string,
# Python will allocate a new memory address for the
# modified string.
print(id(course))

# Lists are mutable
my_list = [1, 2, 3]
print(id(my_list))
my_list.append(4)
print(id(my_list))

# Formatted strings
first = "Sam"
last = "Smith"
# You can put any valid expression in between curly braces
full = f"{first} {last}"
print(full)
