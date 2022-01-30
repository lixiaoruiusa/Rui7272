class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = nums
        if not numbers:
            return []

        numbers.sort()
        if numbers[0] == numbers[-1] and numbers[0] != 0:
            return []

        res = []
        for i in range(len(numbers) - 2):
            if i != 0 and numbers[i] == numbers[i - 1]:
                continue

            left = i + 1
            right = len(numbers) - 1
            while left < right:
                if numbers[i] + numbers[left] + numbers[right] == 0:
                    res.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                elif numbers[i] + numbers[left] + numbers[right] < 0:
                    left += 1
                else:
                    right -= 1
        return res
