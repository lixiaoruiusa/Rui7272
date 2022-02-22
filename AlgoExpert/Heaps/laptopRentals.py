# O(nlogn) time | O(n) space
# 思路： 时间扫描线法， 开始时间+1，结束时间-1， sort一下，打擂台统计最大cost
# 思路2： 先sorted，然后把 (end, start)放入heap中，有overlap的时候push，没overlap 就pop然后push
def laptopRentals(times):
    intervals = []
    for x, y in times:
        intervals.append([x, 1])
        intervals.append([y, -1])
    intervals = sorted(intervals)

    res = 0
    running_cost = 0
    for time, cost in intervals:
        running_cost += cost
        res = max(res, running_cost)
    return res


