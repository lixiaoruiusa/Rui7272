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
        is_prime = [False] * n
        for i in range(2, n):
            if not is_prime[i]:
                count += 1
                for j in range(2, n):
                    if j * i >= n:
                        break
                    is_prime[i * j] = True
        return count


    def countPrimes(self, n):

        if n <= 2: return 0

        is_prime = [True} * n
        is_prime[0] = is_prime[1] = False
        is_prime[2] = True

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime)


