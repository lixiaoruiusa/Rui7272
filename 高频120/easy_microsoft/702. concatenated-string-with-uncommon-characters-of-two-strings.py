class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    @ Time O(n**2), Space O(n)
    """
    def concatenetedString(self, s1, s2):
        res = []
        for char in s1:
            if char not in s2:
                res.append(char)
        for char in s2:
            if char not in s1:
                res.append(char)
        return ''.join(res)