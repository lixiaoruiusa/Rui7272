# 题意：找两个sorted数组的中位数
# 思路：
"""
# 二刷
# Time O(min(n,m))
1 目的是确定数组A和B的分割线的位置，因为两个左边一共贡献（m+n）/2个的元素
2  L1|R1 和 L2|R2 要满足L1<= R2, L2 <= R1
3 在短的数组上 binary search, 因为时间尽量小
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        size1 = len(nums1)
        size2 = len(nums2)

        if size1 > size2:
            return self.findMedianSortedArrays(nums2, nums1)

        # 在短的数组上二分，找正确的分割线
        left = 0
        right = size1

        # 正确分割线的性质有L1|R1,L2|R2, 要找到L1 <= R2 and L2 <= R1的平衡的点
        # 左右元素相同 或 左比右多一个（奇数情况） 故line1 + line2 = (size1+size2+1)//2
        while left < right:
            line1 = (left + right) // 2
            line2 = (size1 + size2 + 1) // 2 - line1

            if nums1[line1] < nums2[line2 - 1]:  # 往右找 R1 < L2
                left = line1 + 1
            else:
                right = line1  # 往左找

        # 出循环后left就是标准分割线位置了
        line1 = left
        line2 = (size1 + size2 + 1) // 2 - line1

        # 为避免分割线某一边没有元素 我们将这种情况下的数定义为正无穷或负无穷 以避免在后续的比较被选出
        L1 = (-float('inf') if line1 == 0 else nums1[line1 - 1])
        R1 = (float('inf') if line1 == size1 else nums1[line1])
        L2 = (-float('inf') if line2 == 0 else nums2[line2 - 1])
        R2 = (float('inf') if line2 == size2 else nums2[line2])

        if (size1 + size2) % 2 != 0:
            return max(L1, L2)
        else:
            return (max(L1, L2) + min(R1, R2)) / 2


# 1 在短的数组上二分, 不断刷选找到line1和line2的标准分割位置， 最终要找到  nums2[line2-1] < nums1[line1] 和 nums1[line1 - 1] < nums2[line2]的位置
# 2 line1 = left， line2 = (size1 + size2 + 1) // 2 - line1  因为求的是两个数组中位数，
# 3 判断line1和line2 的停止位置，分别在0 和len(a), 0 和len(b)的情况。
# 4 nums1LeftMax，nums1RightMin，nums2LeftMax，nums2RightMin的大小值不能确定，需要比较得出结果
# Time O(min(n,m))
# Space O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 为了降低时间复杂度，我们永远使用最小的数组划分
        if len(nums1) > len(nums2):
            # 将最小的数组记作nums1
            return self.findMedianSortedArrays(nums2, nums1)

        # 获取两个数组的长度
        size1 = len(nums1)
        size2 = len(nums2)

        '''
        定义分割线line1 line2 
        1. nums1[line1]表示分割线右边的第一个元素 
        2. nums1[line1-1]表示分割线左边的第一个元素 

        分割线的性质:
        1. nums1[line1] >= nums2[line2-1] and nums1[line-1]<=nums2[line2]
        2. 分割线左右元素相同 或 左比右多一个（奇数情况） 故line1 + line2 = (size1+size2+1)//2
        '''

        # 我们从nums1上进行二分查找分割线
        left = 0
        right = size1

        # 通过这个循环二分查找 不断筛选最终可以得到分割线位置
        while left < right:
            line1 = (left + right) // 2
            line2 = (size1 + size2 + 1) // 2 - line1

            # nums1[line1] < nums2[line2-1] and nums1[line-1] > nums2[line2]不可能同时出现
            # 因此我们只选取一个条件进行筛选即可
            # 如果nums1分割线右边第一个元素偏小 则分割线右移 向右半区查找分割线 否则往左半区
            if nums1[line1] < nums2[line2 - 1]:
                # 此时的分割线一定不是标准分割线 因此下一次查找区间[line1+1 , right]
                left = line1 + 1
            else:
                # 此时的分割线有可能是标准分割线 因此下一次查找区间[left , line1] 即当前位置要保留
                right = line1

        # 出循环后left就是标准分割线位置了
        line1 = left
        line2 = (size1 + size2 + 1) // 2 - line1

        # 确定分割线左边的最大元素和分割线右边的最小元素
        # 为避免分割线某一边没有元素 我们将这种情况下的数定义为正无穷或负无穷 以避免在后续的比较被选出
        nums1LeftMax = (-float('inf') if line1 == 0 else nums1[line1 - 1])
        nums1RightMin = (float('inf') if line1 == size1 else nums1[line1])
        nums2LeftMax = (-float('inf') if line2 == 0 else nums2[line2 - 1])
        nums2RightMin = (float('inf') if line2 == size2 else nums2[line2])

        # 如果总数是奇数 分割线左边最大的元素即为中位数
        # 如果总数是偶数 分割线左边最大的元素和右边最小元素的均值即为中位数
        if (size1 + size2) % 2 != 0:
            return max(nums1LeftMax, nums2LeftMax)
        else:
            return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2


# 方法1： merge两个数组，再找median
# time O(m + n)
# space O(m + n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i = 0
        j = 0
        nums = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < len(nums1):
            nums += nums1[i:]
        if j < len(nums2):
            nums += nums2[j:]

        if len(nums) % 2 != 0:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2

