# Time complexity: O(N)
# Space complexity: O(1)

class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        if queryIP.count('.') == 3:
            return self.valid_ip4(queryIP)
        elif queryIP.count(':') == 7:
            return self.valid_ip6(queryIP)
        else:
            return "Neither"

    def valid_ip4(self, s):

        if not s:
            return "Neither"

        nums = s.split(".")
        # if len(nums) != 4:
        #     return "Neither"

        for num in nums:
            # 00 情况
            if len(num) > 1 and num[0] == "0":
                return "Neither"

            if not num.isdigit():
                return "Neither"

            x = int(num)
            if x < 0 or x > 255:
                return "Neither"

        return "IPv4"

    def valid_ip6(self, s):

        if not s:
            return "Neither"
        nums = s.split(":")
        # if len(nums) != 8:
        #     return "Neither"

        hexdigits = '0123456789abcdefABCDEF'
        dic = Counter(hexdigits)

        for num in nums:
            if not num or len(num) > 4:
                return "Neither"

            for ch in num:
                if ch not in dic:
                    return "Neither"

        return "IPv6"
