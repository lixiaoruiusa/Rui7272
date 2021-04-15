# O(n) time | O(n) space
# array sorted
def sortedSquaredArray(array):

    res = []
    left = 0
    right = len(array) - 1

    while left <= right:

        if abs(array[left]) > abs(array[right]):
            res.append(abs(array[left] ** 2))
            left += 1
        else:
            res.append(abs(array[right] ** 2))
            right -= 1

    return res[::-1]