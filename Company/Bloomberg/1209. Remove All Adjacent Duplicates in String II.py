# O(n) time | O(n) space for the stack.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        if not s:
            return ""

        stack = []  # char, freq
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1

            if stack[-1][1] == k:
                stack.pop()

        res = []
        for c, freq in stack:
            res.append(c * freq)

        return "".join(res)
