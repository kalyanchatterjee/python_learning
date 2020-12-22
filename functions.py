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


print(increment(5, 2))
print(add(4, 5))
# Usage of key word arguments
print(someFunction(original=5, by=2))
print(incrementAgain(5, 2))
