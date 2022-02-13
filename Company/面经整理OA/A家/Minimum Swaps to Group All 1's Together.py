# O(n) time | O(1) space
# 1 长度为total num of 1的sliding window从开始扫
# 2 一直cnt_one 和 max_one 打擂台
# 3 total num of 1 减去 max_one的值就是结果（因为有多少个0，就是最少min swap的数）

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        if not data:
            return -1

        ones = sum(data)

        left = 0
        right = 0

        max_one = 0
        cnt_one = 0

        while right < len(data):
            cnt_one += data[right]

            if right - left + 1 > ones:
                cnt_one -= data[left]
                left += 1
            max_one = max(max_one, cnt_one)
            right += 1
        return ones - max_one

