#  O(log(N)+k) time and O(k) space
# N is number of array, k is length of result.

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        A = arr
        target = x
        right = self.findUpperClosest(A, target)
        left = right - 1

        # 两根指针从中间往两边扩展，依次找到最接近的 k 个数
        results = []
        for _ in range(k):
            if self.isLeftCloser(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        results.sort()
        return results

    def findUpperClosest(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        if A[start] >= target:
            return start

        if A[end] >= target:
            return end

        # 找不到的情况
        return len(A)

    def isLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target