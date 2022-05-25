"""
第一题：把一个string中相邻并重复的字母删掉，不同位置的花费不同，求最小花费。
例如：“aabbcc"和[$1,$2,$1,$2,$1,$2]，删城”ABC"，花费￥3；“aaaa"和【$3,$4，￥5，￥6】，删掉前三个A，花费￥3+4+5
"""

# 1578. Minimum Time to Make Rope Colorful
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        if not neededTime:
            return

        max_value = neededTime[0]
        running_sum = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                if neededTime[i] >= max_value:
                    running_sum += max_value
                    max_value = neededTime[i]
                else:
                    running_sum += neededTime[i]
            else:
                max_value = neededTime[i]

        return running_sum
