https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph/solution/bing-cha-ji-by-iimmortall-buip/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.cnt = n

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y
        self.cnt -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        return uf.cnt

