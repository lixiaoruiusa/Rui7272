# 题意： 猜数字： 数字和位置都对num + A, 数字猜对位置不对用num + B
# 思路：(先求A，把不在正确位置的数字用字典求B)
# 1 循环一遍，把相等位置的secret和guess数量求出来，即为A。同时，把不相等的值放入两个dic中
# 2 循环字典，都在两个字典内的数字，取min值，即为B
# O(n) time n is length of secret or guess
# O(1) space 最多0-9
class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        dic1 = {}
        dic2 = {}
        a = 0
        b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                dic1[secret[i]] = dic1.get(secret[i], 0) + 1
                dic2[guess[i]] = dic2.get(guess[i], 0) + 1

        for num in dic1:
            if num in dic2:
                b += min(dic1[num], dic2[num])

        res = str(a) + "A" + str(b) + "B"
        return res
