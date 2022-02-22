# O(nlogk + k) time | O(n + k) space
# where n is total elements and k is number of arrays
import heapq
def mergeSortedArrays(arrays):
    if not arrays or not arrays[0]:
        return

    res = []
    heap = []

    for i in range(len(arrays)):
        # (-124, 0, 2) (num, index of array ,index of arrays)
        heapq.heappush(heap, (arrays[i][0], 0, i))

    while heap:
        num, index_of_array, index_of_arrays = heapq.heappop(heap)
        res.append(num)
        if index_of_array == len(arrays[index_of_arrays]) - 1:
            continue
        heapq.heappush(heap, (arrays[index_of_arrays][index_of_array + 1], index_of_array + 1, index_of_arrays))
    return res