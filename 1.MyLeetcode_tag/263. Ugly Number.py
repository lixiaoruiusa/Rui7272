# 题意：只有公约数为2 3 5的数 为丑数
# 思路：如果 % 2 == 0，则一直 //2到底， 同理3， 5，判断最后是否得1
class Solution:
    def isUgly(self, n: int) -> bool:

        if n == 0:
            return False

        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5

        if n == 1:
            return True
        return False
