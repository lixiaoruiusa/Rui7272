class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    @ 时间复杂度：O(n∗2^n)，其中n为nums的长度。生成所有子集，并复制到输出集合中。
    @ 空间复杂度：O(n∗2^n)，其中n为nums的长度。存储所有子集，共n个元素，每个元素都有可能存在或者不存在。
    """

    def subsets(self, nums) -> object:
        # write your code here
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


# array = [1,2,3]
# p1 = Solution()
# p1.subsets(array)
'''
[]
<class 'list'>
[1]
<class 'list'>
[1, 2]
<class 'list'>
[1, 2, 3]
<class 'list'>
end dfs
end dfs
[1, 3]
<class 'list'>
end dfs
end dfs
[2]
<class 'list'>
[2, 3]
<class 'list'>
end dfs
end dfs
[3]
<class 'list'>
end dfs
'''

