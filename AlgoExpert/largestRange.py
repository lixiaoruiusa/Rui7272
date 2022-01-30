"""
O(n) time | O(n) space
所有元素存入dic中，检查所有元素数值--和++ 是否在dic中
"""


def largestRange(array):
    result = []
    longest_range = 0
    array = list(set(array))
    dic = {}

    for num in array:
        dic[num] = True

    for num in array:
        if dic[num] is False:
            continue
        dic[num] = False
        count = 1
        left = num - 1
        right = num + 1
        while left in dic:
            dic[left] = False
            count += 1
            left -= 1
        while right in dic:
            dic[right] = False
            count += 1
            right += 1
        if count > longest_range:
            result = [left + 1, right - 1]
            longest_range = count
    return result

