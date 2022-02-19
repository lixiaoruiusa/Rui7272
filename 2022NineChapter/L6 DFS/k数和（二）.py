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

    # 题意： 找出和为target的 k个数的组合
    # 思路： 看有没有重复数，每次把符合target remain 为0的combination加结果
    # 注意： i + 1 是不重复向后选， i 是重复向后选， index + 1是所有从头选

    def kSumII(self, A, k, target):
        if not A:
            return []
        combinations = []
        self.dfs(A, k, target, combinations, [], 0)
        return combinations

    def dfs(self, A, k, remain_target, combinations, combination, index):
        if remain_target == 0 and len(combination) == k:
            combinations.append(list(combination))
            return
        if remain_target < 0 or len(combination) >= k:
            return

        for i in range(index, len(A)):
            combination.append(A[i])
            print(combination)
            self.dfs(A, k, remain_target - A[i], combinations, combination, i + 1)
            combination.pop()


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

"""