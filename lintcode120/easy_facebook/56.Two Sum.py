class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    @Time O(n) Space O(n)
    """
    def twoSum(self, numbers, target):
        if len(numbers) < 2:
            return []
        dic = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dic:
                return [dic[target - numbers[i]],i]
            else:
                dic[numbers[i]] = i