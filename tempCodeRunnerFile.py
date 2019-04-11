non_divisible_tuples = filter(lambda item: (
    item[0] + item[1]) % k != 0, all_tuples)

print(list(non_divisible_tuples))