def sameBsts(arrayOne, arrayTwo):
    if not arrayOne and not arrayTwo:
        return True
    if len(arrayOne) != len(arrayTwo):
        return False
    print(arrayOne, arrayTwo)
    if arrayOne[0] != arrayTwo[0]:
        return False

    left1, right1 = get_divide(arrayOne)
    left2, right2 = get_divide(arrayTwo)

    return sameBsts(left1, left2) and sameBsts(right1, right2)


def get_divide(array):
    smaller = []
    bigger = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
        else:
            bigger.append(array[i])
    return smaller, bigger