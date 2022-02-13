# O(n) time | O(1) space
# 双指针 https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/
# 1 起始的L和R，已经是当前位置L和R的最多水位，无论怎样移动R，都没有意义（因为min(l,r) * t, t会越来越小），所以必须移动小的那边
# 2 移动值小的指针，打擂台 res, cur_res

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        res = 0
        while left < right:
            cur_res = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            res = max(res, cur_res)
        return res
