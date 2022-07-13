import collections


def find_k_distance(start, k, graph):

    if k == 0:
        return [start]

    q = collections.deque([start])
    visited = set()
    visited.add(start)
    distance = 0
    res = []

    while q:
        size = len(q)
        for i in range(size):
            cur = q.popleft()
            if distance == k:
                res.append(cur)
                continue

            for node in graph[cur]:
                if node not in visited:
                    q.append(node)
                    visited.add(node)
        distance += 1
    return res


if __name__ == '__main__':
    graph = {"a": ["b", "d"],
             "b": ["a", "d", "c"],
             "c": ["b", "e"],
             "d": ["a", "e"],
             "e": ["c", "d"]}
    a = find_k_distance("a", 2, graph)
    print(a)
    b = find_k_distance("a", 0, graph)
    print(b)
