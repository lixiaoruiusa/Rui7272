# @ math: 埃拉托斯特尼筛法
# @ Time: O(nloglogn) Space O(n)

class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False

        res = 0
        for i in range(2, n):
            if not is_prime[i]:
                continue
            else:
                res += 1
            for j in range(2 * i, n, i):
                is_prime[j] = False

        return res
