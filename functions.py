def increment(number, by):
    # In Python we can return multiple values
    # Simply put them in parenthesis
    return number, number + by


def add(x, y):
    # Even if there is no return statement, the function
    # returns None
    pass


def someFunction(original, by):
    return original, original + by


def incrementAgain(number: int, by: int) -> int:
    return number + by


def multipleArgs(first, second, third, *rest):
    print("--- Multiple Args ---")
    print(first)
    print(second)
    print(third)
    # By default, variable 'rest' is a tuple
    print(rest)
    print(list(rest))
    for item in list(rest):
        print(item)


def keyWordArgs(**user):
    if (user.get("id") == 1):
        print("Hello, Sam!")
    else:
        print("Hello, You!")


print(increment(5, 2))
print(add(4, 5))
# Usage of key word arguments
print(someFunction(original=5, by=2))
print(incrementAgain(5, 2))
multipleArgs(1, 2, 3, 4, 5, 6)
keyWordArgs(id=4, name="Sam")
