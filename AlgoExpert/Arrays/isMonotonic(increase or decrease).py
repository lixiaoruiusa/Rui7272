def isMonotonic(array):
    increase = True
    decrease = True

    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            increase = False

        if array[i + 1] > array[i]:
            decrease = False

    return increase or decrease

