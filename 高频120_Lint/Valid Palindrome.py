class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    @ Time O(n)  Space O(1)
    """
    def isPalindrome(self, s):
        # write your code here
        if not s: return True
        
        s = s.lower()
        start = 0
        end = len(s) - 1
        
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True