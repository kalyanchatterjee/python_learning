import math

numbers = [1, 3, 4, 8, 13, 15, 18, 23, 35, 47, 49, 51, 57, 63, 68, 71, 89, 98]

start = 0
end = len(numbers) - 1
return_index = -1

input = 98

while start <= end:
    mid = math.ceil((start + end)/2)
    if input == numbers[mid]:
        return_index = mid
        break
    elif input > numbers[mid]:
        start = mid + 1
    else:
        end = mid - 1

print(return_index)
