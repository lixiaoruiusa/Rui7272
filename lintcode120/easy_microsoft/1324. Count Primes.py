class Solution:
    """
    @param n: a integer
    @return: return a integer
    @ math: 埃拉托斯特尼筛法
    @ Time: O(nloglogn) Space O(n)
    """
    def countPrimes(self, n):
        if n <= 2:
            return 0
        count = 0
        not_prime = [False] * n
        for i in range(2,n):
            if not_prime[i] == False:
                count += 1
                for j in range(2,n):
                    if j*i >= n:
                        break
                    not_prime[i*j] = True
        return count