# 给一个数子，可正可负。一定包含至少一个5，一定至少两位数。
# 求 只去掉一个5之后最大的数字
import math
def oa3(num: int):
    result = -math.inf
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] == "5":
            after_remove = num_str[:i] + num_str[i + 1:]
            result = max(result, int(after_remove))
    return result

print(oa3(-9995))
print(oa3(15859))
print(oa3(-15853))
print(oa3(5000))

