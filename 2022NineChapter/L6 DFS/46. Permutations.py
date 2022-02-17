# Time O(N×N!) and a bit slower than (N!)  so it is N!/(N-K)!
# Space O(N!) since one has to keep N! solutions.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        results = []
        self.dfs(nums, [], results)
        return results

    def dfs(self, nums, cur_result, results):
        if len(nums) == len(cur_result):
            results.append(list(cur_result))
            return

        for num in nums:
            if num not in cur_result:
                cur_result.append(num)
                self.dfs(nums, cur_result, results)
                cur_result.pop()
