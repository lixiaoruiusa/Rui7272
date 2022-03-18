class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {1}
        while n not in dic:
            dic.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1

    # def digitsum(self,n):
    #     result = 0
    #     for num in str(n):
    #         result = result + int(num)**2
    #     return result

