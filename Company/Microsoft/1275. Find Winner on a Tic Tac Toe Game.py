# Time complexity: O(m⋅n)
# Space complexity: O(n^2)

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        grid = [[0 for col in range(3)] for row in range(3)]

        for i in range(len(moves)):
            x, y = moves[i]
            if i % 2 == 0:
                fill = 'X'
            else:
                fill = 'O'
            grid[x][y] = fill

        for row in range(3):
            if grid[row][0] == grid[row][1] == grid[row][2] != 0:
                return "A" if grid[row][0] == "X" else "B"

        for col in range(3):
            if grid[0][col] == grid[1][col] == grid[2][col] != 0:
                return "A" if grid[0][col] == "X" else "B"

        if grid[0][0] == grid[1][1] == grid[2][2] != 0 or grid[2][0] == grid[1][1] == grid[0][2] != 0:
            return "A" if grid[1][1] == "X" else "B"

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"