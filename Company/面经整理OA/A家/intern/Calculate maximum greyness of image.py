"""
# Calculated the total number of 1s in each row and each column (row_1s array and col_1s array) using simple prefix array
# number of 0s in a row = m - number of 1s
# let number of 1s in ith row is x and number of 1s in jth colum is y then number of 0s in ith row = m - x and number of 0s in jth column = n - y
# greyness = (x + y) - (m - x + n - y) = 2*(x + y) - (m + n)
# used nested for loops to iterate over all pixels and checked for the maximum greyness overall.
# Time Complexity: O(m*n)
# Space Complexity: O(n)
"""
# column_sums = [sum([row[i] for row in M]) for i in range(0,len(M[0]))]
# row_sums = [sum(row) for row in M]

#def calculate_maximum_greyness(pixels):

pixels = ["101", "001", "110"]
row_1s = []
col_1s = []
m = len(pixels)
n = len(pixels[0])

for i in range(m):
    total_row = 0
    for j in range(n):
        if pixels[i][j] == "1":
            total_row += 1
    row_1s.append(total_row)

for j in range(n):
    total_col = 0
    for i in range(m):
        if pixels[i][j] == "1":
            total_col += 1
    col_1s.append(total_col)

max_greyness = float("-inf")
for i in range(m):
    for j in range(n):
        greyness = 2 * (row_1s[i] + col_1s[j]) - (m + n)
        print(greyness)
        if greyness > max_greyness:
            max_greyness = greyness
return max_greyness

# print(max_greyness)

