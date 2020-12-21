class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    @ 1 二分搜索时每次都是把数组分成两部分，先判段哪一部分是有序的
      2 如果target在有序的那一部分，那么继续二分
      3 如果在无序的那一部分，重复第一步
    Time : log(N)  Space (N)
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
                    
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1