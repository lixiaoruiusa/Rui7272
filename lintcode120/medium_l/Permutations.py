class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    @ time O(n*n!)    space (n!)
    """
    '''
    # solution1: recursion
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return 
        
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    '''
    
    # solution2: Recursion
    def permute(self, nums):
        if not nums:
            return [[]]
            
        permutations = []
        self.dfs(nums, [], set(), permutations)
        return permutations
        
    def dfs(self, nums, permutation, visited, permutations):
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return
        
        for num in nums:
            if num in visited:
                continue
            permutation.append(num)
            visited.add(num)
            self.dfs(nums, permutation, visited, permutations)
            visited.remove(num)
            permutation.pop()
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        