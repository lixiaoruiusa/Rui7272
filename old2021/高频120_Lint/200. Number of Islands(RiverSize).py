def riverSizes(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                result.append(dfs(matrix, i, j))
    return result


def dfs(matrix, i, j):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != 1:
        return 0
    if matrix[i][j] == 1:
        matrix[i][j] = "#"
        return 1 + dfs(matrix, i + 1, j) + dfs(matrix, i - 1, j) + dfs(matrix, i, j + 1) + dfs(matrix, i, j - 1)
