"""
Time Complexity : O(N⋅2^N), where N is the length of string s
N = 3, total nodes = 2^N = 8

Space Complexity: O(N)
For s = aaa, the maximum depth of the recursive call stack is 3 which is equivalent to N
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        if not s:
            return []
        result = []
        self.dfs(result, [], 0, s)
        return result


    def dfs(self, result, path, index, s):
        if index == len(s):
            result.append(path[:])
            return

        for i in range(index, len(s)):
            substr = s[index:i + 1]
            if not self.is_palindrome(substr):
                continue
            path.append(substr)
            self.dfs(result, path, i + 1, s)
            path.pop()

    def is_palindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


