"""
Time: N^(target/min)
n为集合中数字个数，min为集合中最小的数字
每个位置可以取集合中的任意数字，最多有target/min个数字。
Space: N^(target/min)
n为集合中数字个数，min为集合中最小的数字
对于用来保存答案的列表，最多有N^(target/min)种组合
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    # 递归的定义：在candidates[start ... n-1] 中找到所有的组合，他们的和为 target
    # 和前半部分的 combination 拼起来放到 results 里
    # （找到所有以 combination 开头的满足条件的组合，放到 results）
    def dfs(self, candidates, target, start, combination, results):
        # 递归的出口：target <= 0
        if target < 0:
            return

        if target == 0:
            # deepcooy
            return results.append(list(combination))

        # 递归的拆解：挑一个数放到 combination 里
        for i in range(start, len(candidates)):
            # [2] => [2,2]
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            # [2,2] => [2]
            combination.pop()  # backtracking


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates or not target:
            return []

        candidates = sorted(list(set(candidates)))
        result = []
        self.dfs(candidates, target, result, [], 0)
        return result

    def dfs(self, candidates, remain_target, result, path, start_idx):

        if remain_target == 0:
            result.append(list(path))
            return

        if remain_target < 0:
            return

        for i in range(start_idx, len(candidates)):
            path.append(candidates[i])
            self.dfs(candidates, remain_target - candidates[i], result, path, i)
            path.pop()
