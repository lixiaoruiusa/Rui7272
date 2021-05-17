import heapq
'''
a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(a)
print(a)
# [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]

print(heapq.heappop(a))
print(a)
# [1, 3, 2, 6, 9, 5, 4, 7, 8]
heapq.heappush(a, 0)
print(a)
# [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]

print(heapq.nsmallest(3, a))
print(heapq.nlargest(3, a))
'''

a = [1, 2, 3, 9, 10]
b = [6, 7, 8, 14, 15]
c = [4, 5, 11, 12, 13,16,17]

result = []
heap = []
i = 0
j = 0
k = 0
# heapq.heappush(heap, [a[i],i,'a'])
# heapq.heappush(heap, [b[j],j,'b'])
# heapq.heappush(heap, [c[k],k,'c'])
# result.append(heapq.heappop(heap))
# print(heap)
# print(result)

while i < len(a) - 1 or j < len(b) - 1 or k < len(c) - 1:
    if not heap and i == j == k == 0:
        heapq.heappush(heap, [a[i], i, 'a'])
        heapq.heappush(heap, [b[j], j, 'b'])
        heapq.heappush(heap, [c[k], k, 'c'])
    else:
        if result[-1][2] == "a" and i < len(a) - 1:
            i += 1
            heapq.heappush(heap, [a[i], i, 'a'])
        if result[-1][2] == "b" and j < len(b) - 1:
            j += 1
            heapq.heappush(heap, [b[j], j, 'b'])
        if result[-1][2] == "c" and k < len(c) - 1:
            k += 1
            heapq.heappush(heap, [c[k], k, 'c'])

    result.append(heapq.heappop(heap))
    print(heap)
    print(result)

print(heap)
print(result)
sorted_value = []
for res in result:
    sorted_value.append(res[0])
print(sorted_value)

# complexity -> NlogK?
# K = number of lists
# N = number of elements in all lists
# space = O(N)
