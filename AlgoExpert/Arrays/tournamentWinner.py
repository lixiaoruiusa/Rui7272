def tournamentWinner(competitions, results):

    dic = {}

    for i in range(len(results)):
        if results[i] == 0:
            team = competitions[i][1]
        else:
            team = competitions[i][0]

        if team not in dic:
            dic[team] = 3
        else:
            dic[team] += 3

    max_key = max(dic, key=dic.get)

    return max_key


# dic = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
# max_key = max(dic, key=dic.get)
# print(max_key)
# max_value = max(dic.values())
# print(max_value)

# c
# 3

# res = []
# max_value = max(dic.values())
# for k in dic:
#     if dic[k] == max_value:
#         res.append(k)
# print(res)