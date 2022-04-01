"""
把palindrome 破坏掉，用一个字母改了。
思路：
贪心，循环n//2个元素（因为改中心位也没有用）把不是a的元素改成a，就胜利了。
如果没有返回，证明这个palindrome全a，把最后一个元素改成b就胜利了
Time complexity: O(N)
Space complexity: O(N)

"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        n = len(palindrome)
        if n <= 1:
            return ""

        palindrome = list(palindrome)

        # 前面能改成‘a’，就改成'a'。----贪心
        # 因为改掉一个a就不是palindrome

        for i in range(n // 2):

            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        # 前面全是'a'，就该最后一个值为b，就破坏了palindrome
        palindrome[-1] = 'b'
        return ''.join(palindrome)

