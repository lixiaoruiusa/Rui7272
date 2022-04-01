"""
题意：暴力找可能的数字，结果升序排列
思路：
1 counter s中字母的频率
2 {z, w, u, x, g} 对应 0,2,4,6,8 中出现，不信统计一下
3 h 只在 3, 8 中出现。已知 8 出现的次数，可以计算出 3 出现的次数。
  f 只在 4, 5 中出现。已知 4 出现的次数，可以计算出 5 出现的次数。
  s 只在 6, 7 中出现。已知 6 出现的次数，可以计算出 7 出现的次数。

4 求1和9
# letter "i" is present in "nine", "five", "six", and "eight"
# letter "n" is present in "one", "nine", and "seven"

Time complexity : O(N)
Space complexity : O(1)
"""


class Solution:
    def originalDigits(self, s: 'str') -> 'str':
        # building hashmap letter -> its frequency
        count = collections.Counter(s)

        dic = {}
        # 先统计 02468即 zwuxg 的数量，放入结果dic中
        dic["0"] = count["z"]
        dic["2"] = count["w"]
        dic["4"] = count["u"]
        dic["6"] = count["x"]
        dic["8"] = count["g"]

        # 在统计357的个数，h只在3，8 中， f只在4 5中，s只在6 7中
        dic["3"] = count["h"] - dic["8"]
        dic["5"] = count["f"] - dic["4"]
        dic["7"] = count["s"] - dic["6"]

        # letter "i" is present in "nine", "five", "six", and "eight"
        dic["9"] = count["i"] - dic["5"] - dic["6"] - dic["8"]
        # letter "n" is present in "one", "nine", and "seven"
        dic["1"] = count["n"] - dic["7"] - 2 * dic["9"]

        print(dic)
        # {'0': 1, '2': 1, '4': 0, '6': 0, '8': 0, '3': 0, '5': 0, '7': 0, '9': 0, '1': 1}

        res = []
        for key in sorted(dic.keys()):
            cur_res = key * dic[key]
            res.append(cur_res)

        return "".join(res)
