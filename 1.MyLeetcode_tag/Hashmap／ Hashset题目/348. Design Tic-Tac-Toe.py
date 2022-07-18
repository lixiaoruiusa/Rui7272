"""
Time Complexity: O(1)
Space Complexity: O(n)
because we use arrays rows and cols of size n.
The variables diagonal and antiDiagonal use constant extra space.
"""
class TicTacToe:

    def __init__(self, n: int):

        self.n = n      # total number
        self.row = [0 for _ in range(n)]
        self.col = [0 for _ in range(n)]
        self.diagonal = 0
        self.anti_diagonal = 0


    def move(self, row: int, col: int, player: int) -> int:

        # assign the value of 1 for player 1 and -1 for player 2
        if player == 1:
            player_val = 1
        else:
            player_val = -1

        self.row[row] += player_val
        self.col[col] += player_val

        # 正对角线
        if row == col:
            self.diag += player_val
            if abs(self.diag) == self.n:
                return player      # win case 1
        # 斜对角线
        # 因为2 0,1 1,0 2 ==> n - 1 - row
        if (self.n - 1 - row) == col:
            self.anti_diag += player_val
            if abs(self.anti_diag) == self.n:
                return player # win case 2

        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n:
            return player      # win case3, 4

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


"""
Time Complexity: O(1)
every move, we mark a particular row, column, diagonal, and anti-diagonal in constant time
Space Complexity: O(n * n + 2n)
"""
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.grid = [[0 for _ in range(n)] for _ in range(n)]

        self.row = [0 for _ in range(n)]
        self.col = [0 for _ in range(n)]
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:

        if player == 1:
            player_val = 1
        else:
            player_val = -1

        if self.grid[row][col] != 0:
            return "invalid"
        self.grid[row][col] = player_val

        # check if win
        if row == col:
            self.diagonal += player_val
            if abs(self.diagonal) == self.n:
                return player

        if row + col == self.n - 1:
            self.anti_diagonal += player_val
            if abs(self.anti_diagonal) == self.n:
                return player

        self.row[row] += player_val
        self.col[col] += player_val

        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n:
            return player

        # 没胜利时return 0
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)