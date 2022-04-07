"""
思路：
因为题目只有以下三种情况，所以计算和累加running res。
用Flag = False 如果当前stack中的左括号已经计算过了，最后一定会有足够的右括号来pop已经计算过的左括号
当有新的左括号进来的时候，flag = True, 证明又有新的数字要计算。


2**(d-1) 就是该得的结果
三种情况：

()()() = 2**0 + 2**0 + 2**0
((())) = 1 * 2 * 2 = 4 = 2**2
((()())) = (()()) + (()()) = 2**2 + 2**2

Time: O(n)
Space: O(n/2)

"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        if not s:
            return

        stack = []
        res = 0
        flag = False

        for ch in s:

            if ch == '(':
                stack.append(ch)
                flag = True
            else:
                stack.pop()
                if flag:
                    d = len(stack)
                    res += int(2 ** d)
                    flag = False

        return res

# 优化空间
# stack可以用一个running_muti 代替
# 可以到O(1) space
# class Solution:
#     def scoreOfParentheses(self, s: str) -> int:
#
#         if not s:
#             return
#
#         res = 0
#         flag = False
#         running_muti = 0
#
#         for ch in s:
#
#             if ch =='(':
#                 flag = True
#                 running_muti += 1
#             else:
#                 running_muti -= 1
#                 if flag:
#                     d = running_muti
#                     res += int(2**d)
#                     flag = False
#
#         return res
