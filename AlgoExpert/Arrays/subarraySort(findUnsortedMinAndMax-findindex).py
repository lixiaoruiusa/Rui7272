# 1 find unsorted numbers of max and min numbers.
# 2 find the final postion of max and min numbers
# O(n) Time and O(1) Space

def subarraySort(array):
    unsorted_max = float('-inf')
    unsorted_min = float('inf')

    for i in range(len(array)):
        print(unsorted_min, unsorted_max)

        if i == 0 and array[i] > array[i + 1]:
            unsorted_max = max(unsorted_max, array[i])
            unsorted_min = min(unsorted_min, array[i])

        if i == len(array) - 1 and array[i] < array[i - 1]:
            unsorted_max = max(unsorted_max, array[i])
            unsorted_min = min(unsorted_min, array[i])

        if 0 < i < len(array) - 1 and (array[i] < array[i - 1] or array[i] > array[i + 1]):
            unsorted_max = max(unsorted_max, array[i])
            unsorted_min = min(unsorted_min, array[i])

    if unsorted_max == float('-inf') or unsorted_min == float('inf'):
        return [-1, -1]

    left = 0
    right = len(array) - 1
    while unsorted_min >= array[left]:
        left += 1
    while unsorted_max <= array[right]:
        right -= 1

    return [left, right]




