"""
https://leetcode.cn/problems/ugly-number-iii/solution/pyrong-chi-yuan-li-er-fen-zhou-qi-you-hu-8aiq/
思路：二分查找 数学
设一个数字x，小于等于x的丑数个数是：
x//a+x//b+x//c- x//lcm(a,b) - x//lcm(b,c) - x//lcm(a,c) + x // lcm(a, b, c)
其中lcm为最小公倍数。上面公式中的前半部分“x//a+x//b+x//c”比较容易理解，就是x中a,b,c的倍数之和。
然后，对于a,b,c的最小公倍数“x//lcm(a,b) x//lcm(b,c) x//lcm(a,c)”，因为计算a,b,c的倍数时已经统计过一次，此时需要减掉
最后，lcm(a, b, c)是3个数的最小公倍数，第2步减去的2个数的公倍数还可能会重复减，此时需要再加上。

知道了任意一个数字x中丑数的个数，已知x的上下界为[1,2*10^9]，那么可以用二分查找了。
时间复杂度：O(log(2*10^9))
空间复杂度：O(1)
"""
"""
时间复杂度O(logn)
最小公倍数lcm
least common multiple
"""

# Python Program to find the L.C.M. of two input number
# def compute_lcm(x, y):
#    greater = max(x, y)
#    while True:
#        if greater % x == 0 and greater % y == 0:
#            lcm = greater
#            break
#        greater += 1
#
#    return lcm


# 二分法
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = 2 * 10 ** 9

        ans = 0
        while left <= right:
            x = (left + right) // 2

            # 计算小于等于x的丑数的个数
            count = x // a + x // b + x // c - x // lcm(a, b) - x // lcm(a, c) - x // lcm(b, c) + x // lcm(a, b, c)

            if count >= n:
                ans = x
                right = x - 1
            else:
                left = x + 1

        return ans