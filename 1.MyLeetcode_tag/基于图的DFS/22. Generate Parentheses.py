"""

Time Complexity : O(4^n / root n）
如果不在递归过程中进行括号合法判断的话，时间复杂度为 O(2^N)。
N对括号的合法序列的种类数是C(N)，在递归过程中进行合法性判断的话是O(C(N))。

Space Complexity ：O(n)
n的space 存结果
dfs中，最多递归 2n 层，因此空间复杂度为 O(n)

思路：
1 只add左括号，如果left < n
2 只add右括号，如果 right < left
3 如果left == n and right == n，就加入到结果
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        left = right = n
        self.dfs(res, n, [], 0, 0)
        return res

    def dfs(self, res, n, path, left, right):

        if left == n and right == n:
            res.append("".join(list(path)))
            return

        if left < n:
            path.append("(")
            self.dfs(res, n, path, left + 1, right)
            path.pop()

        if right < left:
            path.append(")")
            self.dfs(res, n, path, left, right + 1)
            path.pop()