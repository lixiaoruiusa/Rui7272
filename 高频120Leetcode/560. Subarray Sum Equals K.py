class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        dic = {0: 1}

        for i in range(len(nums)):
            print(i, dic)
            prefix_sum += nums[i]

            if prefix_sum - k in dic:
                count += dic[prefix_sum - k]

            if prefix_sum in dic:
                dic[prefix_sum] += 1
            else:
                dic[prefix_sum] = 1

        return count

