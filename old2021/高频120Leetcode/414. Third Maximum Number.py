class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = list(set(nums))

        res = [float('-inf')] * 3

        for num in nums:
            if num > res[0]:
                res = [num, res[0], res[1]]
            elif num > res[1]:
                res = [res[0], num, res[1]]
            elif num > res[2]:
                res = [res[0], res[1], num]

        if float('-inf') in res:
            return max(res)
        else:
            return res[2]
