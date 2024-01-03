"""
Time Complexity: (2^N)
Space Complexity: O(N)

"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates or not target:
            return []

        candidates = sorted(candidates)

        result = []
        self.dfs(candidates, target, result, [], 0)
        return result

    def dfs(self, candidates, remain_target, result, path, start_index):
        if remain_target < 0:
            return

        if remain_target == 0:
            result.append(list(path))
            return

        for i in range(start_index, len(candidates)):

            # 去重
            if i > start_index and candidates[i - 1] == candidates[i]:
                continue

            path.append(candidates[i])
            self.dfs(candidates, remain_target - candidates[i], result, path, i + 1)
            path.pop()
