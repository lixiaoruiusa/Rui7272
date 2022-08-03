"""
https://leetcode.cn/problems/dota2-senate/solution/dota2-can-yi-yuan-by-leetcode-solution-jb7l/
时间复杂度：O(n)
空间复杂度：O(n)，即为两个队列需要使用的空间
思路： 两个队列，把index分别对应入栈
每次把小的头 + n append到最后，把两个头popleft掉
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()


        return "Radiant" if radiant else "Dire"

