class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for i in range(len(num)):
            while k and stack and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k:
            stack.pop()
            k -= 1

        return ''.join(stack).lstrip("0") or '0'

#       if not stack:
#           return "0"
#       return str(int("".join(stack)))