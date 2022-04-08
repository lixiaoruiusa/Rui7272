"""
DFS
1 count_parentheses, 求不valid的左右括号的数量
2 DFS 中 start为开始的index
出口：left == 0 and right == 0 而且 is_valid


Time Complexity : O(2^N)
其中 n 为字符串的长度。考虑到一个字符串最多可能有 2^n个子序列，每个子序列可能需要进行一次合法性检测
Space Complexity : O(N^2)
其中 n 为字符串的长度。返回结果不计入空间复杂度，考虑到递归调用栈的深度，并且每次递归调用时需要复制字符串一次
"""


class Solution:
    def removeInvalidParentheses(self, s):
        res = []
        left, right = self.count_parentheses(s)
        self.dfs(s, 0, left, right, res)
        return res

    def dfs(self, s, start, left, right, res):
        if left == 0 and right == 0:
            if self.is_valid(s):
                res.append("".join(list(s)))  # res.append(s[:])
                return

        for i in range(start, len(s)):
            # 去重 保证连续多个的时候只删除第一个
            if i > start and s[i] == s[i - 1]:
                continue
            if s[i] == '(' or s[i] == ')':
                curr = s[: i] + s[i + 1:]
                # try all possible to remove right, to keep the prefix valid  like ")("
                if right > 0 and s[i] == ')':
                    self.dfs(curr, i, left, right - 1, res)
                elif left > 0 and s[i] == '(':
                    self.dfs(curr, i, left - 1, right, res)

                # if s[i] == '(':
                #     self.dfs(curr, i, left - 1, right, res)
                # if s[i] == ')':
                #     self.dfs(curr, i, left, right - 1, res)

    def count_parentheses(self, s):
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            if c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right

    def is_valid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            if c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0


# BFS
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         if not s:
#             return ['']
#         queue = deque([s])
#         result, visited = [], set([s])
#         found = False
#         while queue:
#             cur = queue.popleft()
#             if self.is_valid_parentheses(cur):
#                 found = True
#                 result.append(cur)
#             elif not found:
#                 for i in range(len(cur)):
#                     if cur[i] == '(' or cur[i] == ')':
#                         t = cur[:i] + cur[i + 1:]
#                         if t not in visited:
#                             queue.append(t)
#                             visited.add(t)
#         return result
#
#     def is_valid_parentheses(self, s):
#         cnt = 0
#         for c in s:
#             if c == '(':
#                 cnt += 1
#             elif c == ')':
#                 if cnt == 0:
#                     return False
#                 cnt -= 1
#         return cnt == 0
