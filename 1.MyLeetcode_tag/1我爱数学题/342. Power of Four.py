# 题意： 求一个数是不是4次幂后的数
"""
If num is a power of four x = 4^a
then
a = log4(x) = 1/2 log2(x)  is an integer
换地公式log2（15） = lg 15 / lg 2
check if log2x is an even number

"""

# Time complexity : O(1)
# Space complexity : O(1)
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n <= 0:
            return False

        if math.log2(n) % 2 != 0:
            return False

        return True
