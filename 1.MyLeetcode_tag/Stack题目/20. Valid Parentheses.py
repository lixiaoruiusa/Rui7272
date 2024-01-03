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


# class Solution:
#     def isValid(self, s: str) -> bool:
#
#         if not s:
#             return True
#
#         dic = dict()
#         dic["("] = ")"
#         dic["["] = "]"
#         dic["{"] = "}"
# 
#         stack = []
#         for ch in s:
#             # 是右
#             if ch in dic.values():
#                 if not stack or dic[stack[-1]] != ch:
#                     return False
#                 stack.pop()
#             # 是左
#             else:
#                 stack.append(ch)
#
#         return not stack