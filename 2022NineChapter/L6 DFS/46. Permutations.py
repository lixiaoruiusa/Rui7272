# Time O(N×N!) and a bit slower than (N!)  so it is N!/(N-K)!
# Space O(N!) since one has to keep N! solutions.
# 题意：全排列，nums中无重复元素
# 思路：dfs里for loop中，判断num not in permutation即可，所以无需传入index
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []
        permutations = []
        self.dfs(nums, permutations, [])
        return permutations

    def dfs(self, nums, permutations, permutation):

        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return

        for num in nums:
            if num not in permutation:
                permutation.append(num)
                self.dfs(nums, permutations, permutation)
                permutation.pop()