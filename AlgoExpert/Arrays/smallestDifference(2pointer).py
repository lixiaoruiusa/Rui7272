# sort 然后从头两个比大小, 小的后移指针
def smallestDifference(arrayOne, arrayTwo):
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    i = 0
    j = 0
    res = []
    smallest = float('inf')
    current = float('inf')

    while i < len(arrayOne) and j < len(arrayTwo):
        num1 = arrayOne[i]
        num2 = arrayTwo[j]
        if num1 < num2:
            current = num2 - num1
            i += 1
        elif num1 > num2:
            current = num1 - num2
            j += 1
        else:
            return [num1, num2]

        if current < smallest:
            smallest = current
            res = [num1, num2]

    return res