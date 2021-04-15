# Time O(n)| Space O(1)

def firstDuplicateValue(array):
    for value in array:
        if array[abs(value) - 1] < 0:
            return abs(value)
        else:
            index = abs(value) - 1
            array[index] = array[index] * (-1)
    return -1
