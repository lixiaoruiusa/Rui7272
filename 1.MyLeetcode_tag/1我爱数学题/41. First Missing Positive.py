# Index as a hash key.
# 本题要是n time和 n space的话，可以用set
# 但是显然，要求time n space 1
#
# 1 检查1在不在
# 2 < 0 和 > n 的数全部安排成1
# 把 num = abs(nums[i])， 把nums[num - 1] 安排成负数: -abs(nums[num - 1])
# 返回第一个正数的 i + 1 ； 都正就返回n+1
class Solution:
    def firstMissingPositive(self, nums) -> int:

        if not nums:
            return

        n = len(nums)

        if 1 not in nums:
            return 1

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            num = abs(nums[i])
            # 把位置标记为负值，证明归位了
            nums[num - 1] = -abs(nums[num - 1])
            print(nums)
        for i in range(n):
            if nums[i] > 0:
                # 第一个非负数，就是没归位的
                return i + 1
        return n + 1

# obj = Solution()
# obj.firstMissingPositive([3,4,1,1])
"""
Time O(n)
Space O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return

        new_set = set(nums)
        max_num = max(nums)

        if 1 not in new_set:
            return 1

        for i in range(1, max_num + 1):
            if i not in new_set:
                return i
        return i + 1
"""
"""
交换法：把所有的数组swap的应该的位置
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

"""