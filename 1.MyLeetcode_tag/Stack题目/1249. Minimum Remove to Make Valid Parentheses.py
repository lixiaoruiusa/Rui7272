# 题意：删除最少的括号，使其成为valid的 Input: s = "a)b(c)d" Output: "ab(c)d"
# 思路：其实是找所有不valid的左右括号的位置，所以需要存index。左后remove掉不valid的括号，就是剩下好的结果。
# 用stack把左括号和index入栈，右括号检查是否pair，不pair是入栈。 最后把stack的index们放入set，把不在set的s中的值都加入结果
# Time O(n)
# Space O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        if not s:
            return s

        stack = []
        for index, ch in enumerate(s):
            if ch == "(":
                stack.append([index, ch])
            elif ch == ")":
                if stack and stack[-1][-1] == "(":
                    stack.pop()
                else:
                    stack.append([index, ch])

        index_memo = set()
        for i, ch in stack:
            index_memo.add(i)

        res = []
        for i, ch in enumerate(s):
            if i not in index_memo:
                res.append(ch)

        return "".join(res)


# O(n**2) time
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # 从左至右遍历，删除多余的右括号
        cnt, i = 0, 0
        while i < len(s) and s:
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
                if cnt < 0:
                    s = s[:i] + s[ i +1:]
                    cnt = 0
                    i -= 1 # 字符串往回缩了一位，i要回退一位
            i += 1

        # 从右至左遍历，删除多余的左括号
        cnt, i = 0, len(s) -1
        while i >= 0 and s:
            if s[i] == ')':
                cnt += 1
            elif s[i] == '(':
                cnt -= 1
                if cnt < 0:
                    s = s[:i] + s[i + 1:]
                    cnt = 0
            i -= 1

        return s
