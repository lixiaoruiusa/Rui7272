"""
三. An infrastructure consisting of N cities, numbered from 1 to N, and M bidirectional
roads between them is given. Roads do not intersect apart from at their start and end
points (they can pass through underground tunnels to avoid collisions).
For each pair of cities directly connected by a road, let's define their network rank as the
total number of roads that are connected to either of the two cities.
Write a function:
def solution (A, Br N)
that, given two arrays A, B consisting of M integers each and an integer N, where Ali
and Blil are cities at the two ends of the i-th road, returns the maximal network rank in
the whole infrastructure.
Examples:
1. Given A = [1, 2, 3, 3], B = [2, ‍‍‌‍‌‌‍‍‌‍‌‍‌‌‍‍‍‌‌‍3, 1, 4] and N = 4, the function should return 4. The chosen
cities may be 2 and 3, and the four roads connected to them are: (2, 1), (2, 3), (3, 1), (3,4)

"""

# 只check相连的点
def solution(A, B, N):

    # build graph
    # {1: {2, 3}, 2: {1, 3}, 3: {1, 2, 4}, 4: {3}}
    graph = {n: set() for n in range(1, N + 1)}
    for i in range(len(A)):
        graph[A[i]].add(B[i])
        graph[B[i]].add(A[i])

    max_rank = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if j in graph[i]:
                cur = len(graph[i]) + len(graph[j]) - 1
                max_rank = max(max_rank, cur)
    return max_rank


# A = [1, 2, 3, 3]
# B = [2, 3, 1, 4]
# N = 4
# print(solution(A, B, N))

A = [1, 2, 4, 5]
B = [2, 3, 5, 6]
N = 6
print(solution(A, B, N))

# check了所有的点，无论相连不相连
# def solution(A, B, N):
#
#     # build graph
#     # {1: {2, 3}, 2: {1, 3}, 3: {1, 2, 4}, 4: {3}}
#     graph = {n: set() for n in range(1, N + 1)}
#     for i in range(len(A)):
#         graph[A[i]].add(B[i])
#         graph[B[i]].add(A[i])
#
#     max_rank = 0
#     for i in range(1, N + 1):
#         for j in range(i + 1, N + 1):
#             cur = len(graph[i]) + len(graph[j])
#             if j in graph[i]:
#                 cur -= 1
#             max_rank = max(max_rank, cur)
#     return max_rank
#
#
# A = [1, 2, 3, 3]
# B = [2, 3, 1, 4]
# N = 4
# print(solution(A, B, N))



