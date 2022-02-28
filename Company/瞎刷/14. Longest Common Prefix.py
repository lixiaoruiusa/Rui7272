# 1. 纵向扫描
# 时间复杂度：O(mn) m 表示字符串数组中所有字符串的平均长度，n 表示字符串数组的大小
# 空间复杂度：O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        rows = len(strs)
        cols = len(strs[0])
        for col in range(cols):
            for row in range(rows):
                # len(strs[j]) == i 代表本行的单词长度，已经没有了 例如： ab a
                # 在j这个列中发现了不同元素
                if len(strs[row]) == col or strs[row][col] != strs[0][col]:
                    return strs[0][:col]
        return strs[0]