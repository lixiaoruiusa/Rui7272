# Time O(A+B) and Space O(A+B)
# 1 len(res) >= 2的时候判断是否aa或bb, aa时append(b) b--, bb时append(a) a--
# 2 elif A > B: append(a) a-- ; else append(b) b--

class Solution(object):
    def strWithout3a3b(self, A, B):
        result = []
        while A or B:
            if len(result) >= 2 and result[-1] == result[-2] == "a":
                result.append("b")
                B -= 1

            elif len(result) >= 2 and result[-1] == result[-2] == "b":
                result.append("a")
                A -= 1

            elif A > B:
                result.append("a")
                A -= 1
            else:
                result.append("b")
                B -= 1
        return "".join(result)