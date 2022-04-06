"""
# 题意：Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        Output: 22
        Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# 思路：数字都入栈，字符pop 2 个值计算后入栈（注意num2/num1）
# isnumeric() 和isdigit（）都不能判断负数和小数
"""


# Time Complexity : O(n)
# Space Complexity : O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for item in tokens:

            if item not in ["+", "-", "*", "/"]:
                stack.append(item)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if item == "+":
                    cur = num2 + num1
                if item == "-":
                    cur = num2 - num1
                if item == "*":
                    cur = num2 * num1
                if item == "/":
                    cur = num2 / num1
                stack.append(cur)
        return int(stack[-1])
