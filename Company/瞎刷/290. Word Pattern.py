# Time complexity : O(N)
# Space complexity : O(M + 26) M represents the number of unique words in s

# 把每次的dog放个set中，如果不在字典，却在set中，就False | 例如 abba dogdogdogdog

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if not pattern and not s:
            return True
        if not pattern or not s:
            return False

        pattern = list(pattern)
        s = s.split()

        if len(pattern) != len(s):
            return False

        dic = {}
        visited = set()

        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if s[i] in visited:
                    return False
                dic[pattern[i]] = s[i]
                visited.add(s[i])

            elif dic[pattern[i]] != s[i]:
                return False
        return True


