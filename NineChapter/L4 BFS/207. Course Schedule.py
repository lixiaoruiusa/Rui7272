# Time O(∣E∣+∣V∣) where |V|is the number of courses, and |E|is the number of dependencies.
# Space O(∣E∣+∣V∣)
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegrees = {x: 0 for x in range(numCourses)}
        graph = {x: [] for x in range(numCourses)}

        # print(graph)
        # print(indegree)

        for out_node, in_node in prerequisites:
            indegrees[in_node] += 1
            graph[out_node].append(in_node)

        queue = collections.deque()
        for node in indegrees:
            if indegrees[node] == 0:
                queue.append(node)

        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for node in graph[cur]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)
        # del graph[cur]
        # indegrees[cur] = -1

        for v in indegrees.values():
            if v > 0:
                return False
        return True

