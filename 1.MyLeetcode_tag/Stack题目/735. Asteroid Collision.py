# 题意：找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
# 输入：asteroids = [5,10,-5]
# 输出：[5,10]
# 思路：
# 这题厉害的是用了while else， while条件不满足跑出来的到else中
# 无脑入栈：正数，stack为空，stack[-1] 为负值
# 碰撞： while stack and stack[-1] > 0时发生：# 相等时都损毁；stack里边的大，num损毁；stack里边的小，continue，可能到else中append
# Time O(n)
# Space O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for num in asteroids:
            if num > 0 or not stack or stack[-1] < 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] + num == 0:
                        stack.pop()
                        break
                    elif stack[-1] + num > 0:
                        break
                    elif stack[-1] + num < 0:
                        stack.pop()
                        continue
                else:
                    stack.append(num)

        return stack
