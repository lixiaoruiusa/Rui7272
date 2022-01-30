"""
# O(n) time and O(1) space
loop array中
AB 段中最后一个小于running_max的值的位置是R，
反向loop
BC段中 最后一个大于running_min的值的位置是L。
"""


def subarraySort(array):
    running_max = float("-inf")
    running_min = float("inf")
    n = len(array)
    left = -1
    right = -1

    for i in range(n):
        if array[i] < running_max:
            right = i
        else:
            running_max = array[i]

        if array[n - 1 - i] > running_min:
            left = n - 1 - i
        else:
            running_min = array[n - 1 - i]

    if running_max == float("-inf"):
        return [-1, -1]

    return [left, right]