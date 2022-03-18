# O(n) time and O(1) space
# 1 因为有负数的情况，所以求cur max和min 要调换位置
# 2 因为有0的情况，所以要和当前的nums[i]比较
# 3 res和cur_max打擂台
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return

        res = pre_max = pre_min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                cur_max = max(pre_max * nums[i], nums[i])
                cur_min = min(pre_min * nums[i], nums[i])
            else:
                cur_max = max(pre_min * nums[i], nums[i])
                cur_min = min(pre_max * nums[i], nums[i])

            res = max(res, cur_max)
            pre_max, pre_min = cur_max, cur_min

        return res
