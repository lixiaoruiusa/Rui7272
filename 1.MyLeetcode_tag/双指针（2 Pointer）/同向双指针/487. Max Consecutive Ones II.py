# 题意：Input: nums = [1,0,1,1,0] Output: 4， 有一次转换0成为1的机会
# 思路：sliding window， cnt_zero的数量，while cnt_zero > 1 左指针移动，一直打擂台计算结果
# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if not nums:
            return

        res = 0
        cnt_zero = 0
        dic = {}
        left = 0
        for right in range(len(nums)):
            dic[nums[right]] = dic.get(nums[right], 0) + 1

            if nums[right] == 0:
                cnt_zero += 1

            while cnt_zero > 1:
                dic[nums[left]] -= 1
                if nums[left] == 0:
                    cnt_zero -= 1
                left += 1

            res = max(right - left + 1, res)
        return res

