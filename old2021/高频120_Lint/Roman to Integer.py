class Solution:
    """
    @param s: Roman representation
    @return: an integer
    @ 正向扫，如果是特例就减，不然加，最后一个char的值加入结果中返回
    """
    def romanToInt(self, s):
        # write your code here
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        
        if not s:
            return 0
        
        res = 0
        
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i + 1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        return res + d[s[-1]]
        