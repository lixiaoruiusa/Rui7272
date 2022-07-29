# 题意： Input: nums = [0,0,1,1,1,2,2,3,3,4]  Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# 思路：二刷： left 指针先当比较器，当right ！= left时候，再left + 1被写入填充
# 两个指针往后走，slow从0， fast从1，如果nums[fast] != nums[slow]， 就slow += 1 赋值
# Time： O(n)
# Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1