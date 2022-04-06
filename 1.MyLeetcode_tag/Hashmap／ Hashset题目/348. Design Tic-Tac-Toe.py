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
        self.diag = 0
        self.anti_diag = 0


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