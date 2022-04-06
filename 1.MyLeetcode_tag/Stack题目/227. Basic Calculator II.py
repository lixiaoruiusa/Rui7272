# 题意：模拟一个计算器 Input: s = " 3+5 / 2 ", Output: 5
# 思路：在下一个"+-*/"出现的时候(结尾假设成有+号)，计算前一个"+-*/"； 加减入栈，乘除当场计算入栈。
# 用num保存上一个数字，用pre_op保存上一个操作符。当遇到新的操作符的时候，需要根据pre_op进行操作。乘除的优先级高于加减。所以有以下规则：
# pre_sign是+，把之前的数字num进栈
# pre_sign是-，把之前的数字求反-num进栈
# pre_sign是*，立刻出栈和之前的数字相乘，重新进栈
# pre_sign是/，立刻出栈和之前的数字相除，重新进栈
# O(n) time | O(n) space

class Solution:
    def calculate(self, s: str) -> int:

        if not s:
            return

        stack = []
        num = 0
        pre_sign = "+"

        for i, ch in enumerate(s):

            if ch.isdigit():
                num = 10 * num + int(ch)

            if ch in "+-*/" or i == len(s) - 1:

                if pre_sign == "+":
                    stack.append(num)

                if pre_sign == "-":
                    stack.append(-num)

                if pre_sign == "*":
                    value = stack.pop()
                    value = value * num
                    stack.append(value)

                if pre_sign == "/":
                    value = stack.pop()
                    value = value / num
                    stack.append(int(value))

                pre_sign = ch
                num = 0

        return sum(stack)