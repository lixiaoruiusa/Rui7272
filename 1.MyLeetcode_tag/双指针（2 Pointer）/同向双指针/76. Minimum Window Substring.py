# 题意：找最小的在window的substring，
"""
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""


# 思路：sliding window的方法
# 1 要设置一个cnt，记录达到数量的元素个数，也需要一个window的字典
# 2 while cnt == len(count_t): 计算结果，左指针滑动
# 3 同时要检查是否破坏了cnt，即 if s[left] in count_t and dic[s[left]] == count_t[s[left]] - 1
# Time:  Time Complexity: O(n) n 是s的元素个数，最多sliding window访问2n
# Space: O(t) ，Counter(t)的space

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s:
            return ""
        if not t:
            return s

        res = ""
        length = float("inf")

        dic = {}
        count_t = Counter(t)
        cnt = 0

        left = 0
        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1

            if dic[s[right]] == count_t[s[right]]:
                cnt += 1

            while cnt == len(count_t):
                if len(s[left: right + 1]) < length:
                    res = s[left: right + 1]
                    length = len(s[left: right + 1])

                dic[s[left]] -= 1

                if s[left] in count_t and dic[s[left]] == count_t[s[left]] - 1:
                    cnt -= 1
                left += 1

        return res



