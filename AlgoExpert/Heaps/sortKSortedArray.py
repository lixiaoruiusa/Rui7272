# time O(nlogk) | space O(n + k)
# 题意：所有元素与排好后，最多差k个位置（所以可以用heap把k个元素放入）
# 思路：heap把k个元素放入，当放入k+1时，pop并添加到结果
import heapq
def sortKSortedArray(array, k):
    result = []
    heap = []
    for num in array:
        heapq.heappush(heap, num)
        if len(heap) > k:
            res = heapq.heappop(heap)
            result.append(res)
    while heap:
        res = heapq.heappop(heap)
        result.append(res)
    return result

"""
# time O(nlogk) | space O(n + k)
# 题意：所有元素与排好后，最多差k个位置（所以可以用heap把k个元素放入）
# 思路：heap把k个元素放入，当放入k+1时，pop并添加到结果
import heapq


def sortKSortedArray(array, k):
    heap = []
    for i, num in enumerate(array):
        heapq.heappush(heap, num)
        if len(heap) > k:
            res = heapq.heappop(heap)
            array[i - k] = res
    index = len(array) - k
    if index < 0:
        index = 0
    while heap:
        res = heapq.heappop(heap)
        array[index] = res
        index += 1
    return array
"""






