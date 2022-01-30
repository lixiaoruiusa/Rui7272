n = 2
m = 4


# dp = [float("inf")] * n
# dp2 = [1 for _ in range(6)]
# print(dp)
# print(dp2)

# dp = [[1] * n] * m
# print(dp)
# d = [[1] * n for _ in range(m)]
# print(d)

# string1 = "converting string1 into a list of strings!"
#
# list1 = string1.split(" ")
# print(list1)


def last_remaining(n, m):
    if n == 1: return 0
    return (last_remaining(n - 1, m) + m) % n


print(last_remaining(10, 3))


def last_remaining2(n, m):
    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i
    return last


print(last_remaining2(10, 3))
