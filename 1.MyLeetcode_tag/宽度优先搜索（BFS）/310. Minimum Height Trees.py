# 题意：找哪个node下的Height Trees最小
# 思路：就是一个拓扑排序，degree剩下的点为结果，拎起来的树就最小
# 这是一个无相图，所有的点的degree为被链接的freq
# 两两互相存graph          # graph {0: {1}, 1: {0, 2, 3}, 2: {1}, 3: {1}}
# 把所有的元素freq当value  # degrees {0: 1, 1: 3, 2: 1, 3: 1}
# 最后一层要么剩下两个点，要么剩下一个点。 答案必然是其中之一

# Time Complexity: O(n) n number of node
# Space Complexity: O(n)

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if not edges:
            return [0]

        graph = {x: set() for x in range(n)}
        degrees = {x: 0 for x in range(n)}

        for a, b in edges:
            degrees[a] += 1
            degrees[b] += 1
            graph[a].add(b)
            graph[b].add(a)

        queue = collections.deque()
        for node in degrees:
            if degrees[node] == 1:
                queue.append(node)

        while queue:
            res = []
            for i in range(len(queue)):
                cur = queue.popleft()
                res.append(cur)
                degrees[cur] -= 1
                for node in graph[cur]:
                    degrees[node] -= 1
                    if degrees[node] == 1:
                        queue.append(node)
        return res


