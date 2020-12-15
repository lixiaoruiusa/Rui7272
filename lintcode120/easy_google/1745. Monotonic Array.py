class Solution:
    """
    @param A: a array
    @return: is it monotonous
    @Time : O(n) Space O(1)
    """
    def isMonotonic(self, A):
        if not A:
            return True
        
        increase = decrease = True
        
        for i in range(1, len(A)):
            #check increase
            if A[i] < A[i - 1]:
                increase = False
            
            #check decrease
            if A[i] > A[i - 1]:
                decrease = False
            
        return increase or decrease