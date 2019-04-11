arr = [1, 2, -4, 3, 4, 0, 9, -4]


def plusMinus(arr):
    count = len(arr)
    if (count > 0):
        negatives = filter(lambda value: value < 0, arr)
        positives = filter(lambda value: value > 0, arr)
        zeros = filter(lambda value: value == 0, arr)
        negativesCount = len(list(negatives))
        positivesCount = len(list(positives))
        zerosCount = len(list(zeros))

        # Print 6 decimal places
        print('%.6f' % (negativesCount/count))
        print('%.6f' % (positivesCount/count))
        print('%.6f' % (zerosCount/count))


plusMinus(arr)


def printStairs(n):
    maxSpace = n - 1
    for i in range(n):
        print(maxSpace * ' ' + (i + 1) * '#')
        maxSpace = maxSpace - 1


printStairs(4)
