# for i in range(32):
#     mask = 1 << i
#     print("{0:b}".format(mask))


# strings = ('puppy', 'kitten', 'puppy', 'puppy',
#            'weasel', 'puppy', 'kitten', 'puppy')
# counts = {}
#
# for kw in strings:
#     counts.setdefault(kw, 0)
#     counts[kw] += 1
#
# print(counts)
# for kw in strings:
#     if kw not in counts:
#         counts[kw] = 1
#     else:
#         counts[kw] += 1
import heapq
import collections
S = "aab"

    # create a counter
d = collections.Counter(S)

heap = []
for key, value in d.items():
    heapq.heappush(heap, [-value, key])

print(heap)

res = ""
pre = heapq.heappop(heap)
res += pre[1]

while heap:
    curr = heapq.heappop(heap)
    print(curr)
    res += curr[1]

    pre[0] += 1
    if pre[0] < 0:
        heapq.heappush(heap, pre)
    pre = curr
print(res)
print(pre)
# if len(res) != len(S):
#     return ""
# else:
#     return res