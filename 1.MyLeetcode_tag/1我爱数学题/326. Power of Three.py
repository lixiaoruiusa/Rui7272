# Time complexity : O(log_b(n)) , In our case: O(log3(n))
# Space complexity : O(1)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 0:
            return False
        while n and n % 3 == 0:
            n //= 3
        return n == 1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n <= 0:
            return False

        x = math.log10(n) / math.log10(3)

        if x % 1 == 0:
            return True
        return False


"""
>>> math.log(243,3)
4.999999999999999
# Expected: 5

>>> import math
>>> math.log10(243)/math.log10(3)
5
"""