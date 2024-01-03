# 题意：求array中第k个最大值
# 思路：用heap，存k个值，把小的都pop出去，最后堆顶就是结果
# Time complexity : O(Nlogk).
# Space complexity : O(k) to store the heap elements.
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if not nums:
            return

        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            heapq.heappushpop(heap, num)
        return heap[0]

# 方法二： quick sort整个数组，然后打印第n-k个元素
# Time complexity : O(N^2)
# Space complexity : O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if not nums:
            return
        self.patition(nums, 0, len(nums) - 1)

        n = len(nums)
        return nums[n - k]

    def patition(self, array, start, end):
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
        self.patition(array, start, right - 1)
        self.patition(array, right + 1, end)


