class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    @ time O(n^2), space O(n) 更好的写法？
    """
    def isHappy(self, n):
        if n == 1:
            return True
        dic = {}
        while True:
            dic[n] = 1
            n = sum([int(x) * int(x) for x in list(str(n))])
            if n == 1 or n in dic:
                break
        return n == 1
        
