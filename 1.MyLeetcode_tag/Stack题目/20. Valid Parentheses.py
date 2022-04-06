# 题意：Valid Parentheses
# 思路：把左括号都入栈，当出现右括号检查是否为stack.pop的pair
# Time complexity : O(n)
# Space complexity : O(n)
class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return
        paired = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)

            if ch in [')', '}', ']']:
                if stack == []:
                    return False
                value = stack.pop()
                if value != paired[ch]:
                    return False
        return stack == []

