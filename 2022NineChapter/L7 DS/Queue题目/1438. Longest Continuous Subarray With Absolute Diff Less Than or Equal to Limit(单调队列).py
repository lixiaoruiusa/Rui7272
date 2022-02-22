# 题意： 绝对差不超过限制的最长连续子数组，longest subarray的size
# 思路： 此题用sliding window来计算长度，两个monotonic queue来维持最大值和最小值
# 1 loop num, 让单调队列分别keep最大值和最小值
# 2 超出limit的时候，要move left， 同时要更新min_q和max_q中的最大最小值,  nums[left] pop 出去
# O(n) Time
# O(n) Space
import collections


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_q = collections.deque()
        max_q = collections.deque()

        left = 0
        res = 0

        for right, num in enumerate(nums):
            while min_q and min_q[-1] > num:
                min_q.pop()
            while max_q and max_q[-1] < num:
                max_q.pop()

            min_q.append(num)
            max_q.append(num)

            while max_q[0] - min_q[0] > limit:
                if min_q[0] == nums[left]:
                    min_q.popleft()
                if max_q[0] == nums[left]:
                    max_q.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res

