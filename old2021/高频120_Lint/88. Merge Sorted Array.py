class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    @Time O(n) Space O(1)
    @要点：从最后开始比较大小，大的放在最后
    最后不用判断m是否大于0，如果是m大于0，它已经排在nums1前m个位置上了
    """
    def mergeSortedArray(self, A, m, B, n):
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m -= 1
            else:
                A[m + n - 1] = B[n - 1]
                n -= 1
        if n > 0:
            A[:n] = B[:n]


    # leetcode
    '''
    class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            
        if n > 0:
            nums1[:n] = nums2[:n]
    '''