# O(N) Time | O(1) Space..not more than 26 elements
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)

        if np > ns: return []

        p_count = Counter(p)
        s_count = Counter()

        out_put = []

        for i in range(ns):
            # add one more letter
            # on the right side of the window
            s_count[s[i]] += 1

            # remove one letter
            # from the left side of the window
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1

            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                out_put.append(i - np + 1)

        return out_put

'''
# 1 Build reference counter pCount for string p.
# 2 Move sliding window along the string s:
#  Recompute sliding window counter sCount at each step by adding one letter on the right and removing one letter on the left.
#  If sCount == pCount, update the output list.
# 3 Return output list.
'''