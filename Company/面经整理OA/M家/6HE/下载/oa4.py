'''
给一个字符串, 只包含A, B ,写一个函数处理这个字符‍‍‌‌‌‍‍‌‍‍‌‌‌‌‌‍‍‌‍串,
使这个字符串成为左边全是A，右边全是B，
或者整个字符串都是A 或者都是B，使用delete方法。
如S＝“BAAABAB”， 应该返回2，
删除第一个出现的B与最后出现的A。
这题是地里看见过的，复制粘贴过来了，但还有个要求是删除字母数需要最少
'''


def oa4(s: str) -> int:
    n = len(s)
    left_ones = [0] * (n + 1)
    right_zeros = [0] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if s[i - 1] == "1":
            count += 1
        left_ones[i] = count
    print(left_ones)

    count = 0
    for i in range(n - 1, -1, -1):
        if s[i] == "0":
            count += 1
        right_zeros[i] = count
    print(right_zeros)

    res = float("inf")
    for i in range(n + 1):
        res = min(left_ones[i] + right_zeros[i], res)
    return res

print(oa4("1000110"))
