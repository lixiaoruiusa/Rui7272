
nums = [1,2,3,4,5,6]

def lastRemaining(a,k):
    k = 4
    index = 0
    while len(a) > 1:
        index = (index + (k - 1)) % len(a)
        a.pop(index)
        print(a)
    return a[0]

res = lastRemaining(nums, 4)


"""
dp[i]表示n = i时第i次删除的数字，即[i, m]问题，第一次删除数字后会变成一个[i - 1, m]问题，从第m % i个数字开始
dp[i] = (dp[i - 1] + m % i) % i，m % i 为删除第(m - 1) % i个数字后接下来开始的一个数字

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + m % i) % i
        return dp[n]
"""
"""
数学题，得推：
f(n,m)=[(m-1)%n+x+1]%n
      =[(m-1)%n%n+(x+1)%n]%n
      =[(m-1)%n+(x+1)%n]%n
      =(m-1+x+1)%n
      =(m+x)%n

时间复杂度：O(n)，需要求解的函数值有 nn 个。
空间复杂度：O(1)，只使用常数个变量。
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f
"""
