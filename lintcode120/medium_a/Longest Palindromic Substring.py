class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    1 枚举中心 center，需要两个指针 start， end。
    2 如果 s[start] == s[end]，则 start--，end++，更新答案
    3 重复上一步，直到不相等就停止。
    4 注意：奇数和偶数长度的回文串是不同的，奇数中心是单独的一个字符，偶数的是相邻的两个字符。
    枚举回文中心，复杂度 O(n)。
    向两边延展并 check，复杂度 O(n)。
    总时，时间复杂度为 O(n^2)。
    
    """
    def longestPalindrome(self, s):
        
        res = ""
        
        for i in range(len(s)):
            
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
     
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
