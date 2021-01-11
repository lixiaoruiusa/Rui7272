class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    @时间O(n) 空间 O(n)
    """
    def evalRPN(self, tokens):
        # write your code here
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if token == '+': n = n1 + n2
                if token == '-': n = n1 - n2
                if token == '*': n = n1 * n2
                if token == '/': n = int(n1 / n2)
                stack.append(n)
        return stack[-1]