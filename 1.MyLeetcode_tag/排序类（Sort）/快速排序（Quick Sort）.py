def quickSort(array):
    if not array:
        return
    patition(array, 0, len(array) - 1)
    return array


def patition(array, start, end):
    if start >= end:
        return

    pivot = array[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    array[right], array[start] = array[start], array[right]
    patition(array, start, right - 1)
    patition(array, right + 1, end)



def quickSort(array):
    if not array:
        return
    patition(array, 0, len(array) - 1)
    return array


def patition(array, start, end):
    if start >= end:
        return

    pivot = array[end]
    left = start
    right = end - 1

    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    array[left], array[end] = array[end], array[left]
    patition(array, start, left - 1)
    patition(array, left + 1, end)



