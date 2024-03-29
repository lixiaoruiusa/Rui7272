# O(n^2) time and O(n) space
# 每次i的结果等于 max of 每个dp[j] + 1 的结果
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return

        dp = [1 for _ in nums]
        dp2 = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                # if nums[j] < nums[i] and dp2[i] < dp2[j] + 1:
                #     dp2[i] = dp2[j] + 1

        print(dp)
        print(dp2)
        return max(dp)

    
# follow up
class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums:
            return 0

        # state: dp[i] 表示从左到右跳到i的最长sequence 的长度

        # initialization: dp[0..n-1] = 1
        dp = [1] * len(nums)

        # prev[i] 代表 dp[i] 的最优值是从哪个 dp[j] 算过来的
        prev = [-1] * len(nums)

        # function dp[i] = max{dp[j] + 1},  j < i and nums[j] < nums[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # answer: max(dp[0..n-1])
        longest, last = 0, -1
        for i in range(len(nums)):
            if dp[i] > longest:
                longest = dp[i]
                last = i

        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        print(path[::-1])

        return longest