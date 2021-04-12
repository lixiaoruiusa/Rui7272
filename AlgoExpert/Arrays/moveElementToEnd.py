def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array) - 1

    while left < right:
        if array[right] == toMove:
            right -= 1
        elif array[left] != toMove:
            left += 1
        elif array[left] == toMove:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    return array

