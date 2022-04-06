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
                    # 不再继续循环j了
                    break
                    # else:
            #     if len(word2) < len(word1):
            #         return ""

        print(graph)
        print(indegree)
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