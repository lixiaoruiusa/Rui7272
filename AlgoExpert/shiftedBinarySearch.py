def shiftedBinarySearch(array, target):
    if not array:
        return -1

    left = 0
    right = len(array) - 1

    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid

        if array[mid] > array[left]:
            if array[left] <= target < array[mid]:
                right = mid
            else:
                left = mid
        else:
            if array[mid] < target <= array[right]:
                left = mid
            else:
                right = mid

    if array[left] == target:
        return left
    if array[right] == target:
        return right

    return -1
