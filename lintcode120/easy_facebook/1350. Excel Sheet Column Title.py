class Solution:
    """
    @param n: a integer
    @return: return a string
    @Time O(n) Space O(n)
	
    """
    def convertToTitle(self, n):
        res = ''
        while n > 0:
            n -= 1
            # ord('A') is 65 , Z is 26
            res += chr(n % 26 + ord('A'))
            n //= 26
        return res [::-1]
