# **kwargs allows you to pass keyworded variable length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function.


def kwargs_test(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# point = dict(one=1, two=2)

# print(point)

# kwargs_test(point)
# The above won't work because the kwargs must be in the format key="value". Even though the dictionary object is key:value, it still doesn't meet the key="value" expection and the dictionary item will be considered a positional argument.
kwargs_test(first_name="Kalyan", last_name="Chatterjee")
print("-----")
kwargs_test(first_name="Steve")
