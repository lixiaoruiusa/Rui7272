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
