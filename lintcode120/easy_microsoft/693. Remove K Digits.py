class Solution:
    """
    @param num: a number
    @param k: the k digits
    @return: the smallest number
    @trailing_removed = [s.rstrip("0") for s in listOfNum]
    @leading_removed = [s.lstrip("0") for s in listOfNum]
    @both_removed = [s.strip("0") for s in listOfNum]
    @??? Time: O(nlogn) Space: O(n)
    @ 利用stack，如果递增就append，开始递减就delete，最后如果k还有剩余，delete后k位，返回： "".join(num_stack).lstrip("0") or "0" 
    """
    def removeKdigits(self, num, k):
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"
        # result = "".join(num_stack).lstrip("0")
        # return result if result else "0"
 
     
        
