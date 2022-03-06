# 题意：3sum 把结果放到res里
# 思路：排序后三个指针，此题恶心的点是，为避免重复结果，要把三个指针移动到下一个是，判定是否与之前相等，如果相等，持续++或--
# Time Complexity: (n^2)
# Space： O(n)
# Space from O(logn) to (n), depending on the implementation of the sorting algorithm.
# For the purpose of complexity analysis, we ignore the memory required for the output.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return res