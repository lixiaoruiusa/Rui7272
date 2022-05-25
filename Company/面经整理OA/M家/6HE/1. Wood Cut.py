"""
1，给了两个长度的木头，问边长切成多少可以得到最大的正方形，木头不用全部用完，return这个边长。
例如10，21，return 7，因为21可以切成3段7，10中可以切出一个7。

There are two wooden sticks of lengths A and B respectively. Each of them can be cut
into shorter sticks of integer lengths. Our goal is to construct the largest possible
square. In order to do this, we want to cut the sticks in such a way as to achieve four
sticks of the same length (note that there can be some leftover pieces). What is the
longest side of square that we can achieve?
Write a function:
def solution(A, B)
that, given two integers A, B, returns the side length of the largest square that we can
obtain. If it is not possible to create any square, the function should return 0.
Examples:
1. Given A = 10, B = 21, the function should return 7. We can split the second stick into
three sticks of length 7 and shorten the first stick by 3.
2. Given A = 13, B = 11, the function should return 5. We can cut two sticks of length 5
from each of the given sticks.
3. Given A = 2, B = 1, the function should return 0. It is not possible to make any square
from the given sticks.
4. Given A = 1, B = 8, the function should return 2. We can cut stick B into four parts.
"""


def solution(A, B):
    if not A or not B:
        return 0

    p1 = (A + B) // 4
    if p1 < 1:
        return 0
    p2 = min(A, B)
    p = max(p1, p2)
    left = 0
    right = p

    while left + 1 < right:
        mid = (left + right) // 2
        n = A // mid + B // mid
        if n >= 4:
            left = mid
        else:
            right = mid
    if A // right + B // right >= 4:
        return right
    if A // left + B // left >= 4:
        return left
    return 0


print(solution(10, 21))
print(solution(13, 11))
print(solution(2, 1))
print(solution(1, 8))






