# time O(n)
# space  O(26)
# 1 设置start指针，当字典中的值为2时，start指针++，并减字典里存的值，直到值为1
# 2 记录每个循环中，max（res, i - start + 1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        dic = {}
        start = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

            while dic[s[i]] > 1:
                dic[s[start]] -= 1
                start += 1

            res = max(res, i - start + 1)
        return res