"""
输入：数组 = [1,2,3,4]
k = 2
target = 5
输出： [[1,4],[2,3]]
"""
class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        if not A: return []
        results = []
        self.dfs(A, k, target, 0, [], results)
        return results


    def dfs(self, A, k, remain_target, index, cur_result, results):
        if k == 0 and remain_target == 0:
            results.append(list(cur_result))
            return
        if k == 0 or remain_target <= 0:
            return

        for i in range(index, len(A)):
            cur_result.append(A[i])
            self.dfs(A, k - 1, remain_target - A[i], i + 1, cur_result, results)
            cur_result.pop()