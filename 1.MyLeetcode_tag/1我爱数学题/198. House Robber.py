"""
题意：不能偷相邻的房子


边界条件为：
dp[0]=nums[0]  只有一间房屋，则偷窃该房屋
dp[1]=max(nums[0],nums[1])  只有两间房屋，选择其中金额较高的房屋进行偷窃

思路：
if 偷窃第 k 间房屋，那么就不能偷窃第 k-1 间房屋，偷窃总金额为前 k-2 间房屋的最高总金额与第 k 间房屋的金额之和。
即dp[i−2]+nums[i]

不偷窃第 k 间房屋，偷窃总金额为前 k-1 间房屋的最高总金额。
即dp[i−1]


所以 dp[i]=max(dp[i−2]+nums[i],dp[i−1])
"""


class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]


