def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return (numbers, total)


print(multiply(1, 2, 3, 4))
