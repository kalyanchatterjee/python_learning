# *args is used to send a non-keyworded variable length argument list to the function.
def args_test(name: str, *args):
    print(type(name))
    for arg in args:
        print(arg)


args_test("Kalyan", 1, 2, "boy", "squirrel")
