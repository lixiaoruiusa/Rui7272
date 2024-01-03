"""
Time: 每个元素进队出队都只有一次，所以复杂度是O(N)
Space: 队列里元素最多为N个,所以空间复杂度也是O(N)
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []

        max_q = collections.deque()
        left = 0
        res = []

        for right, num in enumerate(nums):

            while max_q and max_q[-1] < num:
                max_q.pop()
            max_q.append(num)

            if right - left + 1 == k:
                res.append(max_q[0])

                if nums[left] == max_q[0]:
                    max_q.popleft()
                left += 1

        return res

