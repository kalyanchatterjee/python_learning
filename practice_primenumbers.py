import time


# Using Sieve of Eratosthenes
def count_primes(n):
    if n < 2:
        return 0

    nums = [1] * n
    nums[0] = nums[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if nums[i] == 1:
            for j in range(i, n, i):
                if j >= i ** 2 and j % i == 0:
                    nums[j] = 0

    return nums.count(1)


start = time.time()
print(count_primes(100000))
end = time.time()
print(f"Time taken: {end-start}")
