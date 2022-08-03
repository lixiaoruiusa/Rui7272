"""
Input in 2D:
1 0 1
1 1 1
0 1 1

Input = [[1,0,1], [1,1,1], [0,1,1]]

Output:
(0,0) (1,0) (1,1) (2,1) (2,2)
(0,0) (1,0) (1,1) (1,2) (2,2)

if impossible to reach bottom-right corner, print "No paths."
"""


def findPaths(mat):
    if not mat or not mat[0] or mat[0][0] != 1:
        return []
    path = []
    results = []
    dfs(mat, path, 0, 0, results)
    return results

def dfs(mat, path, i, j, results):

    if not (0 <= i < len(mat) and 0 <= j < len(mat[0]) and mat[i][j] == 1):
        return

    # print(path)
    if i == len(mat) - 1 and j == len(mat[0]) - 1:
        path.append((i, j))
        results.append(list(path))
        path.pop()

    path.append((i, j))
    dfs(mat, path, i, j + 1, results)
    dfs(mat, path, i + 1, j, results)
    path.pop()


findPaths([[1,0,1], [1,1,1], [0,1,1]])


















# def findPaths(mat, path, i, j):
#     # base case
#     if not mat or not mat[0]:
#         return "No paths"
#
#     M = len(mat)
#     N = len(mat[0])
#
#     if i == M - 1 and j == N - 1:
#         print(path + [mat[i][j]])
#         return
#
#     # include the current cell in the path
#     path.append(mat[i][j])
#
#     # move right
#     if 0 <= i < M and 0 <= j + 1 < N:
#         findPaths(mat, path, i, j + 1)
#
#     # move down
#     if 0 <= i + 1 < M and 0 <= j < N:
#         findPaths(mat, path, i + 1, j)
#
#     path.pop()
#
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# path = []
# x = y = 0
# findPaths(mat, path, x, y)