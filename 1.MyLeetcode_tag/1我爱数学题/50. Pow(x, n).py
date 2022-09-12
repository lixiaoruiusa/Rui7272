# Time logN  N is n here
# space logN

# 3 ^ 4 = 81
# 从下到上返回 3 => 3 * 3 => 9 * 9
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 底数x 为0的情况
        if x == 0:
            return 0
            # 指数n 为0的情况
        if n == 0:
            return 1

        # n为负数的情况
        if n < 0:
            x = 1 / x
            n = - n

        if n % 2 == 0:

            tmp = self.myPow(x, n // 2)
            return tmp * tmp

        else:
            tmp = self.myPow(x, n // 2)
            return tmp * tmp * x




# Time: log N
# Space: Log 1
class Solution:
    def myPow(self, x: float, n: int) -> float:

        is_neg = False
        if n < 0:
            is_neg = True
            n = -n

        res = 1
        base = x

        while n != 0:
            if n % 2 != 0:
                res = res * base

                base = base * base
            else:
                base = base * base

            n = n // 2

        if is_neg:
            return 1 / res
        return res