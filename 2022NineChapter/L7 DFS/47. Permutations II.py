"""
时间复杂度：
O(n×n!)，这里n为数组的长度。当没有重复元素时，排列数组有n!个，即最深层有n!个叶子节点，而拷贝操作需要n，所以时间复杂度为O(n×n!)
空间复杂度：
O(n×n!) 最差情况下，返回的全排列数组有n!个，每个长度为n
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums = sorted(nums)
        visited = [False] * len(nums)
        permutations = []
        self.dfs(nums, visited, [], permutations)
        return permutations

    def dfs(self, nums, visited, permutation, permutations):
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] is False:
                continue

            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, visited, permutation, permutations)
            permutation.pop()
            visited[i] = False
