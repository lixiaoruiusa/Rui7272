class Solution:
    """
    @param s: a string
    @return: it's index
    @ Time: O(n)  Space: O(n)
    @ Use dict{},先将所有字符扫一遍，保存出现过的字符，然后再扫一遍，遇到第一个出现一次的字符就是答案。
    """
    def firstUniqChar(self, s):
        if not s:
            return -1
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        
        
        index = 0
        for ch in s:
            if dic[ch] == 1:
                return index
            index += 1
        return -1