# 题意：The Skyline Problem, 画大楼的轮廓
# 思路：
"""
扫描线，把[left, -1 * height])   ----保证了高的先被扫在前边
        [right, height])入swapline

用堆记录所有走过的楼：
h < 0，是左边，就push
正数就是right边，就remove
用prev记录上一个建筑的最高高度
# 最高高度发生了变化，就append 结果
"""


# Time complexity : O(NlogN)
# Space complexity : O(N)


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        sweepline = []
        for left, right, height in buildings:
            sweepline.append([left, -1 * height])
            sweepline.append([right, height])

        sweepline = sorted(sweepline)

        res = []
        heap = [0]
        prev = 0
        for x, h in sweepline:
            if h < 0:
                heapq.heappush(heap, h)
            else:
                heap.remove(-h)
                heapify(heap)

            # 加入或删除后当前的最高高度
            curr_max = -heap[0]
            # 最高高度发生了变化
            if curr_max != prev:
                res.append([x, curr_max])

            prev = curr_max

        return res

"""
# Time complexity : O(NlogN)
# Space complexity : O(N)

from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        sweepline = []
        for left, right, height in buildings:
            sweepline.append([left, -1 * height])
            sweepline.append([right, height])
        
        sweepline = sorted(sweepline)

        res = []
        
        running_h = SortedList([0])
        
        prev = 0
        for x, h in sweepline:
            if h < 0:
                running_h.add(h)
            else:
                running_h.remove(-h)
                
            # 加入或删除后当前的最高高度
            curr_max = -running_h[0]
            # 最高高度发生了变化
            if curr_max != prev:
                res.append([x, curr_max])
                
            prev = curr_max

        return res

"""