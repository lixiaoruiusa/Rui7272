"""
3101592
一：[3101] 5 [92]
1 [0-3101] 1 [0-99] 
(a + 1) * base

二：[310] 1 [592]
1 [0-309] 1 [0-999]
2 [310] 1 [0-592]
a * base + b + 1

三：[31] 0 [1592]
1 [0-30] 1 [0-9999]
a * base

# Time complexity: Olog10(n)   number of digits
# Space complexity: O(1)
"""


class Solution:
    def countDigitOne(self, n: int) -> int:

        base = 1
        res = 0
        while base <= n:
            b = n % base
            a = n // base
            cur = a % 10
            a //= 10

            if cur > 1:
                res += (a + 1) * base
            elif cur == 1:
                res += (a * base + b + 1)
            else:
                res += a * base

            base *= 10

        return res



