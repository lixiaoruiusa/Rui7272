# O(n) time | O(1) space
# 1 相向双指针 和 running left_max, right_max
# 2 判断左右两边哪个bar高， count 为累加 running_max - 矮指针值【因为另一边更高，水一定流不出去】
# 3 每次移动矮的指针
class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        count = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                count += left_max - height[left]
                left += 1
            else:
                count += right_max - height[right]
                right -= 1

        return count


# O(n) time | O(n) space
# 1 dp正向和反向的running max数组值
# 2 拼接在一起的时候，min(dp1,dp2) - height的 为水的存量
# 3 count 每个大于0的水量

class Solution:
    def trap(self, height: List[int]) -> int:

        from_left = [0] * len(height)
        from_right = [0] * len(height)

        running_max = float("-inf")
        for i in range(len(height)):
            if height[i] > running_max:
                running_max = height[i]
            from_left[i] = running_max

        running_max = float("-inf")
        for i in reversed(range(len(height))):
            if height[i] > running_max:
                running_max = height[i]
            from_right[i] = running_max

        count = 0
        for i, num in enumerate(height):
            cur_count = min(from_left[i], from_right[i]) - num
            if cur_count > 0:
                count += cur_count
        return count
