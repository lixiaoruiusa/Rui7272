# 题意：找Container With Most Water的一段，返回总量
# 思路：双指针，计算水量，每次移动短的那边
# 1 起始的L和R，已经是当前位置L和R的最多水位，无论怎样移动R，都没有意义（因为min(l,r) * t, t会越来越小），所以必须移动小的那边
# 2 移动值小的指针，打擂台 res, cur_res
# O(n) time | O(1) space
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        res = float("-inf")

        while left < right:
            if height[left] < height[right]:
                cur_res = height[left] * (right - left)
                res = max(res, cur_res)
                left += 1
            else:
                cur_res = height[right] * (right - left)
                res = max(res, cur_res)
                right -= 1
        return res