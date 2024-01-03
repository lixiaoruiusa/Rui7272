"""
找出一个数组中一个数出现次数和这个数相等的数.
例如 A：[3, 1, 4, 5, 3, 2, 1, 3] return 3，多种情况的话返回最大的数
"""
from collections import Counter
import math
def oa6(a: list[int]) -> int:
    counter = Counter(a)
    result = -math.inf
    for k, v in counter.items():
        if k == v:
            print(f"result is {k}")
            result = max(result, k)
    return result

print(oa6([3,1,4,5,3,2,2,1,3,4,4,4]))