

# 题意：找两个array重合的部分
# 思路：用dict维护前一个数组中每个值出现的次数 然后遍历第二个数组，对于每个遍历到的数，在dict中将这个数出现的次数-1
# Time Complexity: O(n+m)
# Space Complexity: O(min(n,m))  We use hash map to store numbers (and their counts) from the smaller array.
# So Space O(n) or O(m)

# 也可以先排序，然后类似于merge two sorted array的方法，相等才append
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


# Time Complexity: O(n+m)
# Space Complexity: O(n+m)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)

        nums = nums1 + nums2
        nums = list(set(nums))

        result = []
        for num in nums:
            if num in counter1 and num in counter2:
                times = min(counter1[num], counter2[num])
                while times:
                    result.append(num)
                    times -= 1

        return result