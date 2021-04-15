def mergeOverlappingIntervals(intervals):
    if not intervals:
        return [[]]

    intervals = sorted(intervals, key=lambda x: x[0])

    res = []

    for interval in intervals:
        if not res or interval[0] > res[-1][1]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res
