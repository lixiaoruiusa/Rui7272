# O(n) Time , number of elements in s
# O(1) Space
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        if not s:
            return s

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

str1 = "Geeks for Geeks"
a = str1.split()
b = list(str1)
c = str1.replace(' ','')
print(a)
print(b)
print(c)
