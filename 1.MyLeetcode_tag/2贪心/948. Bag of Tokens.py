# Time: O(NlogN) for sorting
# Space: O(N) for sorting new list
# 题意：初始有一个p值，能消耗左边count就+1，否则加成右边count-1，求最大count
# 思路：先sort，然后双指针往中间走。
# 注意最后重合的时候如果要-1，就不计算了，保持贪心。
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        if not tokens: return 0

        left = 0
        right = len(tokens) - 1

        tokens = sorted(tokens)
        res = 0

        if power < tokens[0]:
            return 0

        while left <= right:
            while left <= right and power >= tokens[left]:
                power -= tokens[left]
                res += 1
                left += 1

            if left == right and power < tokens[left]:
                break

            while left <= right and power < tokens[left]:
                power += tokens[right]
                res -= 1
                right -= 1

        return res

