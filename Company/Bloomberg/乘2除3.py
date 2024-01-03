"""
Given an int n. You can use only 2 operations:
multiply by 2
integer division by 3 (e.g. 10 / 3 = 3)
Find the minimum number of steps required to generate n from 1.
"""

# BFS 用q
import collections
def minSteps(n):
    q = collections.deque()
    q.append(1)
    count = 0
    visited = set()
    while q:
        for i in range(len(q)):
            cur = q.popleft()
            if cur == n:
                return count
            if cur not in visited:
                visited.add(cur)
                q.append(cur // 3)
                q.append(cur * 2)

        count += 1
    return count
print(minSteps(11))


