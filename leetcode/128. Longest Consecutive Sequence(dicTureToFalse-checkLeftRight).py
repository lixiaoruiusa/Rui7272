class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))

        dic = {}
        best = []
        longest_length = 0

        for num in nums:
            dic[num] = True

        for num in nums:
            # if not dic[num]:
            #     continue
            if dic[num]:
                dic[num] = False
                current_length = 1
                left = num - 1
                right = num + 1

                while left in dic:
                    dic[left] = False
                    current_length += 1
                    left -= 1

                while right in dic:
                    dic[right] = False
                    current_length += 1
                    right += 1

                if current_length > longest_length:
                    longest_length = current_length
                    best = [left + 1, right - 1]

        return longest_length


