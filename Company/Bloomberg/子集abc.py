class Solution:
    def subsets(self, nums):
        nums = sorted(nums)
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()

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
