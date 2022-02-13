# 請問一下第二題，N = 2
# [1, 2, 2, 2, 1] -> return 4(最後一個1) - 0(第一個1) = 4
# 是這個意思嗎?
# 对的，没错 4 - 0

# counter = {}
# for num in array:
#     counter[num] = counter.get(num, 0) + 1

# O(n) time | O(n) space
# array = [1, 2, 2, 2, 1]
def find_max_index(array):
    if not array:
        return -1

    max_len = float("-inf")
    #max_len = -1
    counter = {}
    for i in range(len(array)):
        if array[i] not in counter:
            counter[array[i]] = [i]
        else:
            counter[array[i]].append(i)

    for values in counter.values():
        if len(values) >= 2:
            max_len = max(max_len, values[-1] - values[0])
    return max_len

