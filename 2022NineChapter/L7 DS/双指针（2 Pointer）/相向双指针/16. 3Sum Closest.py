# 题意：找 3Sum Closest
# 思路：类似于3Sum， 用closest 打擂台，如果cur_sum == target，return 结果，否则继续找
# Time：O(n^2)
# Space Complexity: from O(logn) to O(n)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        closest = float("inf")
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if abs(cur_sum - target) < closest:
                    closest = abs(cur_sum - target)
                    res = cur_sum

                if cur_sum == target:
                    return res
                elif cur_sum > target:
                    right -= 1
                else:
                    left += 1
        return res