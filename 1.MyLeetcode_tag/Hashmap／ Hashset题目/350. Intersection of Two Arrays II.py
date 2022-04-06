# 题意：找两个array重合的部分
# 思路：counter一个数组，loop另一个数组，频率-1，加入结果
# Time Complexity: O(n+m)
# Space Complexity: O(min(n,m))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1 or not nums2:
            return []

        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        res = []
        for num in nums1:
            if num in counter2 and counter2[num] > 0:
                res.append(num)
                counter2[num] -= 1
        return res