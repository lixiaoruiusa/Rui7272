# 题意：给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度
"""
输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
"""
# 思路：
"""
这道题看起来很像是常规滑动窗口套路的问题，但是用普通滑动窗口思路无法解决问题。
1 枚举最长max_unique 从1到26，每种情况进行sliding window计算
2 字典记录窗口的count，distinct_count记录有多少个不同字母，less_k_count记录窗口中小于k频次的数量
3 while distinct_count > max_unique 左边开始滑动，到distinct_count正常为止
检查字母出window和字母不符合k次的情况
4 打擂台比结果 
"""


# Time Complexity : O(maxUnique⋅N) ~ O(26n)~ O(n)
# Space Complexity: O(26) ~ O(1)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        res = 0
        for max_unique in range(1, 27):
            dic = {}
            distinct_count = 0
            less_k_count = 0

            left = 0
            for right in range(len(s)):
                dic[s[right]] = dic.get(s[right], 0) + 1

                if dic[s[right]] == 1:
                    distinct_count += 1
                    less_k_count += 1

                if dic[s[right]] == k:
                    less_k_count -= 1

                while distinct_count > max_unique:
                    dic[s[left]] -= 1
                    # 字母出了window
                    if dic[s[left]] == 0:
                        distinct_count -= 1
                        less_k_count -= 1
                    # 当字母首次达到k-1 说明有一个符合条件k的字母不符合条件了，less+=1
                    if dic[s[left]] == k - 1:
                        less_k_count += 1
                    left += 1

                if distinct_count == max_unique and less_k_count == 0:
                    res = max(right - left + 1, res)
        return res


