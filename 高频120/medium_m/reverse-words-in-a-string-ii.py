class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        if not str:
            return
        # reverse word
        array = list(str)
        array = self.swap(array, 0, len(array) - 1)

        # reverse letter
        index = 0
        for i in range(len(array)):
            if array[i] == ' ':
                self.swap(array, index, i - 1)
                index = i + 1
            
            if i == len(array) - 1:
                self.swap(array, index, i)
        
        # Convert list to string
        return ''.join(array)
        
    
    
    def swap(self, array, left, right):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        return array
            
