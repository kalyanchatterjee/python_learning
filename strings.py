course = "Programming in Python"
# print(id(course))
# course = course.lower()
# print(id(course))

# print(id(course))
# print(id(course.lower()))

# # Title case
# print(course.title())

# find() is case sensitive
print(course.find("Py"))

course_lower = course.lower()
print(course_lower.find("Py"))
print(course_lower.find("py"))

print(id(course_lower))
# basic data types are IMMUTABLE
print(id(course_lower.replace("p", "P")))

print("Programming" in course)
