"""
时间复杂度：n * 2^n 其中n为nums的长度。
生成所有子集，并复制到输出集合中
空间复杂度：
n * 2^n，其中n为nums的长度。
存储所有子集，共 n个元素，每个元素都有可能存在或者不存在。

"""
class Solution:
    def subsets(self, nums):
        nums = sorted(nums)
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, index, subset, subsets):
        subsets.append(list(subset))

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()


nums = ["a", "b", "c"]
# s = "a b c"
# ss = "abc"
# s1 = s.split()
# s2 = list(ss)
# print(nums)
# print(s1)
# print(s2)

p = Solution()
print(p.subsets(nums))
