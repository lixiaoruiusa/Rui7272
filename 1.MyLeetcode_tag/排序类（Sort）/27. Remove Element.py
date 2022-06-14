
# 二刷：同向双指针，从0开始：right不是target时就swap，因为相当于默认right是target时就skip

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return left


# 题意：把target都move到最后，返回有多少个除了target的元素
# 思路：其实就是同向双指针，if nums[i] != target，yingxie或者交换，类似move zero

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        yingxie = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[yingxie] = nums[i]
                yingxie += 1
        return yingxie


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0
        right = 0

        while right < len(nums):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return left






