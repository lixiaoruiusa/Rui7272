"""
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
题意：
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
有值的情况返回商，e和x不存在，返回-1.0

思路：build_graph + DFS



复杂度分析：
q is number of queries; e number of equations.

Time Complexity: O(q⋅e + e)
For each query, we need to traverse the graph O(q⋅e)
build a graph takes O(e)

Space Complexity: O(e)
build graph is N edges and 2N nodes in the graph, O(3e) ~ O(e)
recursion stack is O(e)
visited is O(e)

"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        if not equations:
            return []


        # build_graph  {'a': [('b', 2.0)], 'b': [('a', 0.5), ('c', 3.0)], 'c': [('b', 0.3333333333333333)]}
        graph = {}
        for i in range(len(equations)):
            if equations[i][0] not in graph:
                graph[equations[i][0]] = [(equations[i][1], values[i])]
            else:
                graph[equations[i][0]].append((equations[i][1], values[i]))

            if equations[i][1] not in graph:
                graph[equations[i][1]] = [(equations[i][0], 1 / values[i])]
            else:
                graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

        print(graph)

        # 初始化一个都为-1.0的结果
        results = [-1.0] * len(queries)

        # 结果为连乘
        for i, query in enumerate(queries):
            if query[0] not in graph or query[1] not in graph:
                continue
            self.dfs(query[0], graph, 1, query[1], i, set([query[0]]), results)

        return results


    def dfs(self, start, graph, res, target, i, visited, results):
        for neighbor in graph[start]:
            if neighbor[0] == target:
                results[i] = res * neighbor[1]
                return
            if neighbor[0] not in visited:
                res *= neighbor[1]
                visited.add(neighbor[0])
                self.dfs(neighbor[0], graph, res, target, i, visited, results)
                res /= neighbor[1]
                visited.remove(neighbor[0])
            