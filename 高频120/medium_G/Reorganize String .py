import heapq
from collections import Counter


class Solution:
    """
    @param S: a string
    @return: return a string
    @ Time: O(nlogn)
    """

    def reorganizeString(self, S):

        if S == "":
            return ""

            # create a counter
        d = collections.Counter(S)

        heap = []
        for key, value in d.items():
            heapq.heappush(heap, [-value, key])

        res = ""
        pre = heapq.heappop(heap)
        res += pre[1]

        while heap:
            curr = heapq.heappop(heap)
            res += curr[1]

            pre[0] += 1
            if pre[0] < 0:
                heapq.heappush(heap, pre)
            pre = curr

        if len(res) != len(S):
            return ""
        else:
            return res