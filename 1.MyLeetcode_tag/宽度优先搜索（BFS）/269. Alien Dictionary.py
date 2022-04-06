# 题意：根据给的 words = ["wrt","wrf","er","ett","rftt"]的顺序，看能不能生成 这个rules的一个排序
# 思路
"""
1 根据所有唯一的letter建graph和indegree
2 循环len(words) - 1， word1 = words[i], word2 = words[i + 1]
3 特别注意边界条件：前边的word比后边的长的话，# like abcd, abc no solution（相当于d指向None了） return ""
4 循环min(len(word1), len(word2))，if word1[j] != word2[j]:建图和入度，break
5 正常bfs 加入res，检查入度是否有剩余。没有的话 return ''.join(res)
"""
# time: O(n) space: O(n)
# number of characters in the dictionary (including duplicates) is n
# Building graph takes O(n) Topological sort takes O(V + E).V <= n.E
# So the overall time complexity is O(n).

import collections
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words: return ""

        nodes = set()
        for word in words:
            for c in word:
                if c not in nodes:
                    nodes.add(c)

        graph = {node: [] for node in nodes}
        indegree = {node: 0 for node in nodes}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            # like abcd, abc no solution
            if len(word2) < len(word1) and word1[:len(word2)] == word2:
                return ""
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    out_node = word1[j]
                    in_node = word2[j]
                    indegree[in_node] += 1
                    graph[out_node].append(in_node)
                    # 不再继续循环j了，因为后边的参考没有意义了，因为这一位已经开始不同了
                    break

        queue = collections.deque()
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for node in graph[cur]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)

        # if len(res) != len(indegree):
        for v in indegree.values():
            if v > 0:
                return ""
        return ''.join(res)