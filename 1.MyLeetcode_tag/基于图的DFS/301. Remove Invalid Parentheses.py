"""
DFS
1 count_parentheses, 求不valid的左右括号的数量
2 DFS 中 start为开始的index
出口：left == 0 and right == 0 而且 is_valid

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
            if i != start and s[i] == s[i - 1]:
                continue
            if s[i] == '(' or s[i] == ')':
                curr = s[: i] + s[i + 1:]
                if right > 0 and s[i] == ')':
                    self.dfs(curr, i, left, right - 1, res)
                elif left > 0 and s[i] == '(':
                    self.dfs(curr, i, left - 1, right, res)

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
