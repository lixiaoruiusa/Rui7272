class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    @ () round brackets or parentheses,
    @ {} called curly brackets or braces,
    @ [] are the square brackets,
    @ Time: O(n)  Space: O(n)
    @ 题意：输入一个只包含括号的字符串，判断括号是否匹配
    模拟堆栈，读到左括号压栈，读到右括号判断栈顶括号是否匹配
    最后return not stack
    """
    def isValidParentheses(self, s):
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                # 栈需非空??
                if not stack:
                    return False
                if ch == ')' and stack[-1] != '(' or ch == ']' and stack[-1] != '[' or ch == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack
