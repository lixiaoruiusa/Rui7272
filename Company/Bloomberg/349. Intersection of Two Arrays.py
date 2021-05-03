from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        Counter1 = Counter(nums1)
        res = []

        for num in nums2:
            if num in Counter1:
                res.append(num)

        return list(set(res))
