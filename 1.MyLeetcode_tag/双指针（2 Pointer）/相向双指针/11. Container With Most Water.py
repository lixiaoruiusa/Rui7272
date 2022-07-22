# 题意：找Container With Most Water的一段，返回总量
# 思路：双指针，计算水量，每次移动短的那边
# 1 起始的L和R，已经是当前位置L和R的最多水位，无论怎样移动R，都没有意义（因为min(l,r) * t, t会越来越小），所以必须移动小的那边
# 2 移动值小的指针，打擂台 res, cur_res
# O(n) time | O(1) space
class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            if height[l] < height[r]:
                cur = height[l] * (r - l)
                l += 1
            else:
                cur = height[r] * (r - l)
                r -= 1
            res = max(res, cur)
        return res