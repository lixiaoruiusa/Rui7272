# DFS
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

"""
# DFS 2
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        
        visited = [[False for col in range(len(board[0]))] for row in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, visited, i, j, 0):
                    return True
        return False
        
        
    def dfs(self, board, word, visited, i, j, index):
        
        if len(word) == index:
            return True
        
        if not (0 <= i < len(board) and 0 <= j < len(board[0]) and word[index] == board[i][j] and not visited[i][j]):
            return False
        
        visited[i][j] = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = i + dx, j + dy
            if self.dfs(board, word, visited, x, y, index + 1):
                return True
        visited[i][j] = False
        return False

"""
"""
DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]
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