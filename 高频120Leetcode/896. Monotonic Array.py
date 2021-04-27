class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        is_increase = True
        is_decrease = True

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                is_decrease = False
            if A[i] < A[i - 1]:
                is_increase = False

        return is_increase or is_decrease
