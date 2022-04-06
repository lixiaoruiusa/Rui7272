# 题意：根据所给的sequences，看是否有唯一的拓扑排序nums
# 思路：
"""
1 求出所有唯一的node
2 建图和indegrees
3 以为有可能多于2个，所以循环到len(sequence) - 1，
out_node = sequence[i]
in_node = sequence[i + 1]
4 正常BFS， if len(queue) > 1: # 证明有分叉，有两个node入度相同，所以肯定不唯一，return False
5 最后是否 res 和 nums相等

# 建图中， O(len(sequences) * max len(sequence) # 空间复杂度O(n)
# BFS 中时间复杂度O(n^2) # 空间复杂度O(n)

"""
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

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
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        res = []
        while queue:
            if len(queue) > 1: # 证明有分叉，有两个node入度相同，所以肯定不唯一
                return False
            cur = queue.popleft()
            res.append(cur)
            for node in graph[cur]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        return res == nums