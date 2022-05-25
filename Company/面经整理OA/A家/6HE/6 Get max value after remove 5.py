# 给一个数子，可正可负。一定包含至少一个5，一定至少两位数。
# 求 只去掉一个5之后最大的数字


def remove_five(n):

    res = float("-inf")
    num = str(n)
    for i in range(len(num)):
        if num[i] == "5":
            cur = num[:i] + num[i + 1:]
            res = max(res, int(cur))
    return res


print(remove_five(-9995))
print(remove_five(15859))
print(remove_five(-15853))
print(remove_five(5000))