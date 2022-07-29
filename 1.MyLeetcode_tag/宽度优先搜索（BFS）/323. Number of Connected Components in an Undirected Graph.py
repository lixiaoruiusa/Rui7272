# Time complexity: O(E+V)  E = Number of edges, VV = Number of vertices
# Space complexity: O(E+V)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                self.bfs(i, graph, visited)
        return count

    def bfs(self, i, graph, visited):
        q = deque([i])
        while q:
            cur = q.popleft()
            for node in graph[cur]:
                if node not in visited:
                    q.append(node)
                    visited.add(node)
