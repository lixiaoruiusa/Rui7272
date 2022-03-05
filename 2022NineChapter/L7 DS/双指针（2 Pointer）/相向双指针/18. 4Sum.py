# 题意：4Sum
# 思路：类似于3sum的思路，四个指针move时： nums[i] == nums[i - 1]要continue
# Time： O (n^3)
# Space: O (n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                Total = target - nums[i] - nums[j]

                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == Total:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > Total:
                        right -= 1
                    else:
                        left += 1

        return res