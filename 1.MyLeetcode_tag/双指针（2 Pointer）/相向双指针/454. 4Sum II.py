# 题意：4Sum II 找4个数组中，和为0的数量
# 思路：counter数组，a和b，c和d， 找counter1中key， -key再counter2中的值，res = res + dic1[key]* dic2[-key]相乘
# 或者再loop c和d的时候把结果一直+ ，like res += counter.get(-c - d, 0)
# Time Complexity: (n^2)
# Space Complexity: O(n^2) distinct a + b keys
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        dic1 = {}
        for a in nums1:
            for b in nums2:
                dic1[a + b] = dic1.get(a + b, 0) + 1

        dic2 = {}
        for c in nums3:
            for d in nums4:
                dic2[c + d] = dic2.get(c + d, 0) + 1

        res = 0
        for x in dic1:
            if -x in dic2:
                res += dic1[x] * dic2[-x]
        return res


"""
answer = 0
for c in C:
    for d in D:
        answer += counter.get(-c - d, 0)
return answer
"""