import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegrees = [0] * numCourses
        # 建图和indegree list
        for i in range(numCourses):
            graph[i] = []

        for i in range(len(prerequisites)):
            to_node, from_node = prerequisites[i]
            indegrees[to_node] += 1
            # if from_node not in graph:
            #     print(here)
            #     graph[from_node] = []
            graph[from_node].append(to_node)

        queue = collections.deque()
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(node)
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for node in graph[cur]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)
            # indegrees[cur] = -1
            # del graph[cur]

        for v in indegrees:
            if v > 0:
                return []
        return res

"""
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegrees = [0] * numCourses
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for node_in, node_out in prerequisites:    
            graph[node_out].append(node_in)
            indegrees[node_in] += 1
        
        res = []
        queue = collections.deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i) 
      
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for node in graph[cur]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)

            # indegrees[cur] = -1
            # del graph[cur]
            
        for num in indegrees:
            if num > 0:
                return [] 
        return res
"""