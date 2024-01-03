"""
给出两个数组A和B，找出index可以使得
A[i] 左边的sum 等于 B[i]左边的sum，同时A[i] 右边的sum 也等于 B[i]右边的sum。‍‌‌‌‍‌‌‍‍‌‌‍‍‍‍‌‌‌
举个栗子， A: [2, 7, -2, 5], B：[-1, 10, 0, 3]，
在index = 3的时候， 2 + 7 = -1 + 10，同时 -2 + 5 = 1 + 3
"""

def oa5(a: list[int], b: list[int]) -> int:
    a_sum = get_left_right_sum(a)
    b_sum = get_left_right_sum(b)
    print(a_sum)
    print(b_sum)
    for i in range(len(a_sum)):
        if a_sum[i] == b_sum[i]:
            return i
    return -1

def get_left_right_sum(a: list[int]) -> list[(int, int)]:
    left_sum = 0
    right_sum = sum(a)
    result = []
    for elem in a:
        left_sum += elem
        right_sum -= elem
        result.append((left_sum, right_sum))
    return result

print(oa5([2,7,-2,5], [-1,10,0,3]))