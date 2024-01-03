# 题意： Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6  Output: 2
# 思路：
# 1 stop_to_bus存   站点：车 {1: {0}, 2: {0}, 7: {0, 1}, 3: {1}, 6: {1}})
# 2 用两个set记录 visited_bus和visited_stop
# 3 start 入队， 把这个stop所有的bus找出来，把未访问过的bus里所有的站入队
# 4 分层遍历找路径
# 时间复杂度：O(m*n) m: # of buses, n: # of routes
# 空间复杂度：O(m*n + m)


import collections
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        # stop：bus {1: {0}, 2: {0}, 7: {0, 1}, 3: {1}, 6: {1}})
        stop_to_bus = defaultdict(set)

        for i in range(len(routes)):
            for stop in routes[i]:
                stop_to_bus[stop].add(i)

        # 把stop的站点入q
        visited_bus = set()
        visited_stop = set()
        queue = deque([])
        queue.append(source)
        visited_stop.add(source)

        # 分层BFS
        count = 0
        while queue:
            size = len(queue)
            for i in range(size):
                stop = queue.popleft()
                if stop == target:
                    return count

                buses = stop_to_bus.get(stop)
                for bus in buses:
                    if bus not in visited_bus:
                        visited_bus.add(bus)

                        for next_stop in routes[bus]:
                            if next_stop not in visited_stop:
                                visited_stop.add(next_stop)
                                queue.append(next_stop)
            count += 1

        return -1