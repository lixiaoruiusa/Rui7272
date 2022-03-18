"""
时间复杂度： O(log_3 n)   n = 3*3*3*3..  so n = 3^k so  k = log_3 n
空间复杂度：O(1)
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n and n % 3 == 0:
            n //= 3
        return n == 1

p1 = Solution()
a = p1.isPowerOfThree(-3)
print(a)

#print(-1 % 3)  # 2
#print(-3 % 3)  # 0