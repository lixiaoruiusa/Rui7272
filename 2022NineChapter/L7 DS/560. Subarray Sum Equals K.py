class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        if not nums: return 0

        dic = {0: 1}
        count = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in dic:
                count += dic[prefix_sum - k]
            dic[prefix_sum] = dic.get(prefix_sum, 0) + 1
        return count
