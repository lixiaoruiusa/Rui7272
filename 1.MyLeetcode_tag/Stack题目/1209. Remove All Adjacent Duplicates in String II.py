# 题意: 类似于糖果消除, 消除string中k个连续字母
# 思路： stack，解法也类似于糖果消除，把[a:1]放入栈中如果相同元素入栈，只更新频率[a:2],到k的时候消除
# 要放list，tuple不能直接修改。
# O(n) time | O(n) space

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])

            elif stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        res = []
        for ch, freq in stack:
            res.extend(ch * freq)
        return "".join(res)
