# O(nlogn) time | O(n) space  N is len(input) array
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None

        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            if interval[1] > result[-1][1]:
                result[-1][1] = interval[1]
        return result

