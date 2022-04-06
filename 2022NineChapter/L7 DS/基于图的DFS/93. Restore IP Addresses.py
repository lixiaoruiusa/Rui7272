"""
"25525511135"
时间复杂度：O(3^4 * s)  因为2，25，255 每层最多3个选择，一共右4层， s为len of s, "".join需要的时间
空间复杂度：O(4)
Space complexity : constant space to keep the solutions, not more than 19 valid IP addresses.
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        self.dfs(s, res, 0, [])
        return res

    def dfs(self, s, res, start_idx, subset):

        if len(subset) == 4 and start_idx == len(s):
            res.append('.'.join(subset))
            return

        for i in range(start_idx, start_idx + 3):
            if i >= len(s):
                return

            substring = s[start_idx: i + 1]

            if self.is_valid(substring):
                subset.append(substring)
                self.dfs(s, res, i + 1, subset)
                subset.pop()

    def is_valid(self, cur):

        if cur == '0':
            return True  # 解决"0000"
        if cur[0] == '0':
            return False  # 不能是01或者011  #if len(cur) != len(str(int(cur))):
        if 0 < int(cur) < 256:  # 必须在0-255之间
            return True
        return False
