# 题意：给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
# 思路：sliding window中， 字典里max_freq 就是 max(dic.values())
# 1 如果 窗口元素和 - 字典里max_freq > k时候，字典--， left ++
# 2 如果窗口元素和 - 字典里max_freq <= k时候，打擂台比较res
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        dic = {}

        left = 0
        for right in range(len(s)):

            dic[s[right]] = dic.get(s[right], 0) + 1

            while (right - left + 1) - max(dic.values()) > k and left < right:
                dic[s[left]] -= 1
                left += 1
            if (right - left + 1) - max(dic.values()) <= k:
                res = max(right - left + 1, res)
        return res





