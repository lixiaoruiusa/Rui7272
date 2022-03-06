# 题意：decode s到传统方式 Input: "3[a]2[bc]" ==> "aaabcbc"
# 思路：用stack：1 数字 放到multi中
#               2 字母 放到res = "" 中
#               3 [ 入栈append，把 muti，res 放入
#               4 ] 出栈pop，把 当前res * muti +
#
# O(n) time | O(n) space
class Solution:
    def decodeString(self, s: str) -> str:

        if not s: return ""

        multi = ""
        res = ""
        stack = []
        for c in s:

            if c.isdigit():
                multi += c
            if c.isalpha():
                res += c
            if c == "[":
                stack.append((multi, res))
                multi = ""
                res = ""
            if c == "]":
                factor, pre_res = stack.pop()
                # if factor != "":
                #     res = res * int(factor)
                res = pre_res + res * int(factor)

        return res
