# 题意：Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 Output: 6， 有k次转换0成为1的机会
# 思路：sliding window， cnt_zero的数量，while cnt_zero > k 左指针移动，一直打擂台计算结果
# Time Complexity: O(N)
# Space Complexity: O(1)

# 二刷
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        res = 0
        left = 0
        cnt = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                cnt += 1

            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


# 一刷
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
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

            while cnt_zero > k:
                dic[nums[left]] -= 1
                if nums[left] == 0:
                    cnt_zero -= 1
                left += 1

            res = max(right - left + 1, res)
        return res
