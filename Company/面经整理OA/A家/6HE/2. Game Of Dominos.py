"""
A game of dominos consists of 28 domino tiles. Between 0 and 6 dots appear at each
end of every tile. Tiles can be reversed during the game, so the tile showing
"2-3"
can
be played as "3-2".
You are given a list of N unique domino tiles. Your task is to find any domino tile not on
the list and return it in the format "X-Y", where X and Y are digits representing the
number of dots on each end of the tile. Note that because domino tiles can be reversed,
tiles "2-3" and "3-2" are treated as the same tile.
Write a function:
func Solution(A []string) string
that, given an array A of N strings representing unique domino tiles, returns a string
representing any tile which is not in the array A. Tiles in A are given in the format
described above. You can assume that there will always exist a tile not listed in A
Examples:
1. Given A = "O-0", "O-1", "2-3", "2-0"], one of the possible outputs is "0-3". Note that
"1-0" is not a valid answer, as "0-1" represents the same tile.
2. Given A = "O-0", "1-1", "2-2", "3-3" "4-4', "5-5" "6-6'), one of the possible outputs is
"2-4"

"""
def Solution(A):
    if not A:
        return "0-0"

    memo = set()
    for s in A:

        a = int(s[0])
        b = int(s[-1])
        memo.add((a, b))
        memo.add((b, a))

    for i in range(7):
        for j in range(7):
            if (i, j) not in memo:
                return str(i) + "-" + str(j)

A = ["0-0", "0-1", "2-3", "2-0"]
B = ["0-0", "1-1", "2-2", "3-3", "4-4", "5-5", "6-6"]
print(Solution(A))
print(Solution(B))