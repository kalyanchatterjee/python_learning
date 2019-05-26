def some_function(arg1, arg2, arg3, *arg, **kwargs):
    print(f"arg1 : {arg1}")
    print(f"arg2 : {arg2}")
    print(f"arg3 : {arg3}")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} : {value}")


args = ("apple", "orange")
# The keys must match with the function definition (order can be random however)
kwargs = {"arg4": "apple", "arg5": "orange", "arg6": "banana"}

# Calling with both
some_function("x", "y", "z", *args, **kwargs)
