class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        index = self.firstIndex(A, target)
        left, right = index - 1, index
        result = []
        for i in range(k):
            #???
            if left < 0:
                result.append(A[right])
                right += 1
            elif right == len(A):
                result.append(A[left])
                left -= 1
            else:
                # 比较间距大小 判断指针移动
                if target - A[left] <= A[right] - target: 
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1
                    
        return result
        
    def firstIndex(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        
        if A[start] >= target:
            return start
            
        if A[end] >= target:
            return end
        
        # 找不到的情况???
        return len(A)