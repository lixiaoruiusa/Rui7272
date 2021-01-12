class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    
    @ Two pointer
    @Time O nlog(n)  Space O(n)
    """
    
    
    def twoSum(self, numbers, target):
        if len(numbers) < 2:
            return []
        new_numbers = enumerate(numbers)
        new_numbers = sorted(new_numbers, key = lambda x: x[1])
        left = 0
        right = len(new_numbers) - 1
        while left < right:
            if new_numbers[left][1] + new_numbers[right][1] == target:
                return sorted([new_numbers[left][0], new_numbers[right][0]])
            elif new_numbers[left][1] + new_numbers[right][1] < target:
                left += 1
            else:
                right -= 1
        return []
