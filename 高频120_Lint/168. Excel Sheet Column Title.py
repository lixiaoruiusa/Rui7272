class Solution:
    """
    @param n: a integer
    @return: return a string
    @ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4
    @ unicode : ord('A') is 65
    @ The chr() method returns a character (a string) from an integer (represents unicode code point of the character).
    @Time O(n) Space O(n)
    @ n - 1 是因为base A 是 1

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        n = columnNumber

        while n > 0:
            n -= 1

            res += chr(n % 26 + ord('A'))
            n //= 26

        return res[::-1]



    def convertToTitle(self, n):
        # write your code here
        # Time O(N), No extra space
        result = ''
        while n > 0:
            if n % 26 == 0:
                result += chr(ord('Z'))
                n -= 26
            else:
                result += chr(ord('A') + n % 26 - 1)
            n /= 26
        return result[::-1]



print()