# Time O(log(m + n)) and Space O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1
        B = nums2

        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(nums1, 0, B, 0, n // 2 + 1)
        else:
            smaller = self.findKth(A, 0, B, 0, n // 2)
            bigger = self.findKth(A, 0, B, 0, n // 2 + 1)
            return (smaller + bigger) / 2


    def findKth(self, A, index_a, B, index_b, k):
        if len(A) == index_a:
            return B[index_b + k - 1]
        if len(B) == index_b:
            return A[index_a + k - 1]
        if k == 1:
            return min(A[index_a], B[index_b])

        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else None
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else None

        if b is None or (a is not None and a < b):
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
        return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)


