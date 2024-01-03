"""
Time: O(nm*3^length)
O(nm)是由于我们要遍历board每个点，判断它是否和word相同
O(3^length)是由于我们dfs过程，四个方向都要去试，但有一个方向是从上一个位置过来的方向，过来的方向是不用去搜索的了
Space: O(L) where L is the length of the word to be matched.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not word:
            return True
        if not word or not board:
            return False

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(word, i, j, board, visited, 0):
                    return True
        return False

    def dfs(self, word, i, j, board, visited, word_idx):

        if word_idx == len(word):
            return True

        if not (0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in visited and word[word_idx] == board[i][
            j]):
            return False

        visited.add((i, j))
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + i
            ny = y + j
            if self.dfs(word, nx, ny, board, visited, word_idx + 1):
                return True
        visited.remove((i, j))

        return False


"""




DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False

        visited = [[False for col in range(len(board[0]))] for row in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0, visited):
                    return True
        return False

    def dfs(self, board, word, i, j, index, visited):
        if index == len(word):
            return True

        if not self.is_valid(board, word, i, j, index, visited):
            return False

        visited[i][j] = True
        for x, y in DIRECTIONS:
            _x = i + x
            _y = j + y
            if self.dfs(board, word, _x, _y, index + 1, visited):
                return True
        visited[i][j] = False
        return False

    def is_valid(self, board, word, i, j, index, visited):
        return (0 <= i < len(board) and 0 <= j < len(board[0]) and not visited[i][j] and word[index] == board[i][j])


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False

        visited = [[False for col in range(len(board[0]))] for row in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.dfs(board, word, i, j, 0, visited):
                        return True
                    visited[i][j] = False
        return False

    def dfs(self, board, word, i, j, index, visited):
        print(board[i][j])
        if index == len(word) - 1:
            return True

        for x, y in DIRECTIONS:
            _x = i + x
            _y = j + y

            if self.is_valid(board, word, _x, _y, index + 1, visited):
                visited[_x][_y] = True
                if self.dfs(board, word, _x, _y, index + 1, visited):
                    return True
                visited[_x][_y] = False
        return False

    def is_valid(self, board, word, i, j, index, visited):
        return (0 <= i < len(board) and 0 <= j < len(board[0]) and not visited[i][j] and word[index] == board[i][j])
"""
