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
        self.dfs(s, res, [], 0)
        return res

    def dfs(self, s, res, path, index):

        if index == len(s) and len(path) == 4:
            res.append(".".join(list(path)))
            return

        if len(path) > 4:
            return

            # 255 - 2,25,255
        for j in range(index, index + 3):
            # j有可能出界，很重要，会导致is_valid的位置溢出
            if j >= len(s):
                return

            substring = s[index: j + 1]
            if self.is_valid(substring):
                path.append(substring)
                self.dfs(s, res, path, j + 1)
                path.pop()


    def is_valid(self, cur):

        if cur == '0':
            return True  # 解决"0000"
        if cur[0] == '0':
            return False  # 不能是01或者011  #if len(cur) != len(str(int(cur))):
        if 0 < int(cur) < 256:  # 必须在0-255之间
            return True
        return False
