# 题意：找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
# 输入：asteroids = [5,10,-5]
# 输出：[5,10]
# 思路：
# 二刷：发生碰撞的条件是：stack里边是正数，cur是负数的时候，才有可能碰撞
# Time O(n)
# Space O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        if not asteroids:
            return []

        stack = []

        for asteroid in asteroids:

            if not stack:
                stack.append(asteroid)
                continue

            cur = asteroid
            # 发生碰撞的条件是：stack里边是正数，cur是负数的时候，才有可能碰撞
            while stack and stack[-1] > 0 and cur < 0:
                prev = stack.pop()
                if prev + cur > 0:
                    cur = prev
                if prev + cur == 0:
                    cur = 0
                if prev + cur < 0:
                    cur = cur

            if cur != 0:
                stack.append(cur)

        return stack
