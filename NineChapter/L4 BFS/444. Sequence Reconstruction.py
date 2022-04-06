# sequences 不是pair，有可能多于2个
# 如果queue中有两个元素，证明有分叉，return False

import collections
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        # 所有node放入set中，loop set，建立graph和indegree
        nodes = set()
        for seq in sequences:
            for node in seq:
                if node not in nodes:
                    nodes.add(node)

        graph = {x: [] for x in nodes}
        indegree = {x: 0 for x in nodes}

        for sequence in sequences:
            for i in range(len(sequence) - 1):
                out_node = sequence[i]
                in_node = sequence[i + 1]

                graph[out_node].append(in_node)
                indegree[in_node] += 1

        queue = collections.deque()
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            if len(queue) > 1:
                return False
            cur = queue.popleft()
            res.append(cur)
            for node in graph[cur]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
            # del graph cur
            # indegree[cur] = -1
        return res == nums