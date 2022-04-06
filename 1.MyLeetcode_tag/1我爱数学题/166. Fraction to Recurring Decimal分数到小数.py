"""
给一个被除数和除数
以字符串形式返回小数 。如果小数部分为循环小数，则将循环的部分括在括号内。

时间复杂度：O(l)，其中l 是答案字符串的长度
空间复杂度：O(l)
思路：
1 先检查正负，把res上加入符号
2 先求整数部分，把first加入结果，如果n % d，返回 ''.join(res)
3 精彩的部分来了，分数部分用字典记录是否remainder出现过，把dic[r] = len(res)正好是括号的位置
每次r*10， 把r//d的结果加入res，如果r为0或者在字典中停止
r为0说明除尽了
如果r在字典中，说明开始循环了
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        n = numerator
        d = denominator
        res = []

        if n * d < 0:
            res.append("-")

        n = abs(n)
        d = abs(d)

        # 整数部分
        frist = n // d
        res.append(str(frist))
        if n % d == 0:
            return ''.join(res)

        # 小数部分
        res.append(".")

        r = n % d
        dic = {}
        while r and r not in dic:
            dic[r] = len(res)
            r *= 10
            res.append(str(r // d))
            r %= d

        if r:  # 有循环节
            insertIndex = dic[r]
            res.insert(insertIndex, '(')
            res.append(')')

        return ''.join(res)
