'''
Time: O(N^(t/m))
n为集合中数字个数，min为集合中最小的数字
每个位置可以取集合中的任意数字，最多有target/min个数字。
Space : O(N^(t/m))
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates, remain_target, index, cur_result, results):
        if remain_target == 0:
            results.append(list(cur_result))
            return

        for i in range(index, len(candidates)):
            if remain_target < candidates[i]:
                return
            cur_result.append(candidates[i])
            self.dfs(candidates, remain_target - candidates[i], i, cur_result, results)
            cur_result.pop()
