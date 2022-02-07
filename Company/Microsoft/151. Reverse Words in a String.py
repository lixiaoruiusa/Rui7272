class Solution:
    def reverseWords(self, s: str) -> str:
        # string_list = s.split()
        # string_list = string_list[::-1]
        # result = " ".join(string_list)
        # return result

        if not s:
            return ""
        s_list = s.split()

        left = 0
        right = len(s_list) - 1
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return " ".join(s_list)