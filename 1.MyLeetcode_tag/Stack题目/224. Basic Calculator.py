class Solution:
    def calculate(self, s: str) -> int:

        res = 0  # 记录running的结果
        num = 0  # 记录当前的数字，有*10的情况
        pre_sign = "+"  # 记录符号,

        stack = []

        for i, ch in enumerate(s):

            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in "+-":
                if pre_sign == "+":
                    res += num

                if pre_sign == "-":
                    res -= num

                pre_sign = ch
                num = 0

            if ch == "(":
                stack.append([res, pre_sign])
                res = 0
                pre_sign = "+"

            if ch == ")":
                if pre_sign == "+":
                    res += num

                if pre_sign == "-":
                    res -= num
                num = 0
                r, p = stack.pop()
                if p == "+":
                    res = r + res
                if p == "-":
                    res = r - res

        # 最后不是括号，还有数的情况
        if pre_sign == "+":
            res += num
        if pre_sign == "-":
            res -= num

        return res
