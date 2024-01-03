"""
思路：1 先整体reverse 再reverse每个单词，与rotate array的思路一样
Time：O(N) 整体N，个体近似O(1)
Space：O(1)
"""
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if not s:
            return []
        self.reverse_nums(0, len(s) - 1, s)
        # from ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        # to ["e","u","l","b"," ","s","i"," ","y","k","s"," ","e","h","t"]

        left = 0
        for right in range(len(s)):
            if s[right] == " ":
                self.reverse_nums(left, right - 1, s)
                left = right + 1

            if right == len(s) - 1:
                self.reverse_nums(left, right, s)
        return s

    def reverse_nums(self, left, right, nums):

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums