# sort(key=lambda x:(x[0],-x[1]))
# 题意：The Skyline Problem, 画大楼的轮廓
# 思路：
"""
扫描线，把[left, -1 * height])   ----保证了高的先被扫在前边
        [right, height])入swapline

用堆记录当前最高的楼，
如果新的h高，就划一笔；
如果堆高；就默默push
当扫到正数h的时候，要把堆里的remove走
"""


# Time complexity : O(NlogN)
# Space complexity : O(N)


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        swapline = []
        for left, right, height in buildings:
            swapline.append([left, -1 * height])
            swapline.append([right, height])

        swapline = sorted(swapline)

        res = []
        heap = [0]

        for x, h in swapline:
            if h < 0:
                tmp = heap[0]
                heappush(heap, h)
                if tmp != heap[0]:
                    res.append([x, -h])

            else:
                tmp = heap[0]
                heap.remove(-h)
                heapify(heap)

                if tmp != heap[0]:
                    res.append([x, -heap[0]])

        return res

