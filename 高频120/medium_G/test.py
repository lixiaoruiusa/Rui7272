# for i in range(32):
#     mask = 1 << i
#     print("{0:b}".format(mask))


strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

for kw in strings:
    counts.setdefault(kw, 0)
    counts[kw] += 1

print(counts)
# for kw in strings:
#     if kw not in counts:
#         counts[kw] = 1
#     else:
#         counts[kw] += 1