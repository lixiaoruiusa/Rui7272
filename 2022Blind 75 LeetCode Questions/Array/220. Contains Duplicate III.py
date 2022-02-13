# O(n) time | O(min(n,k)) space
# 1 对所有数字//t+1 可以把数字装进不同的桶里 且桶里面的数字满足abs(x-y) <= t
# 2 对数组进行遍历，从i到k时，如果有桶里有俩数，很明显满足
# 3 超过k的时候，就需要把i-k的数从桶里删除，因为不再考虑他们了
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        all_bucket = {}

        for i, num in enumerate(nums):

            bucket_number = nums[i] // (t + 1)

            if bucket_number in all_bucket:
                return True

            all_bucket[bucket_number] = num

            if bucket_number - 1 in all_bucket and abs(num - all_bucket[bucket_number - 1]) <= t:
                return True

            if bucket_number + 1 in all_bucket and abs(num - all_bucket[bucket_number + 1]) <= t:
                return True

            if i >= k:
                del all_bucket[nums[i - k] // (t + 1)]
        return False


"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 对所有数字//t+1 可以把数字装进不同的桶里 且桶里面的数字满足abs(x-y) <= t
        # 对数组进行遍历，从i到k时，如果有桶里有俩数，很明显满足
        # 超过k的时候，就需要把i-k的数从桶里删除，因为不再考虑他们了
        all_buckets = {}
        bucket_size = t + 1
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size  # 放入哪个桶

            if bucket_num in all_buckets:  # 桶中已经有元素了
                return True

            all_buckets[bucket_num] = nums[i]  # 把nums[i]放入桶中

            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t:  # 检查前一个桶
                return True

            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t:  # 检查后一个桶
                return True

            # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
            if i >= k:
                all_buckets.pop(nums[i - k] // bucket_size)

        return False
"""