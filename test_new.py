# scores = [1, 2, 3, 4, 5, 4]
# dp1 = [1 for _ in range(len(scores))]
# print(dp1)
# dp2 = [1 for _ in scores]
# print(dp2)


# dp = [1 for _ in range(len(scores))]
#
# for i in range(1, len(scores)):
#     if scores[i] > scores[i - 1]:
#         dp[i] = dp[i - 1] + 1
#
# print(dp)
#
# for i in reversed(range(len(scores) - 1)):
#     print(i)

# import collections
#
# q = collections.deque([1, 2, 3, 4])
# print(5 in q)  # False
# print(1 in q)


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
dp = [[0 for _ in triangle[-1] ] for _ in triangle]
#print(dp)

for i in range(0, len(triangle)):
    for j in range(0, i + 1):
        print(i,j)