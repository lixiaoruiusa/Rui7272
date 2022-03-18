"""
求考试最高的平均分，输入是[["Bob", "90"], ["John", "82"], ["Bob", "96"], ...]，一个人可以有多个成绩，找出平均分最高的分数。
"""
# Time O(n) n is len of scores
# Space O(n) for dic
# # {name:[total, count]}
class Solution:
    def find_maxavg(self, scores):

        dic = {}
        for name, score in scores:
            if name not in dic:
                dic[name] = [0, 0]
            dic[name][0] += int(score)
            dic[name][1] += 1

        res_name = ""
        res_avg_score = float("-inf")
        for key, val in dic.items():
            avg = val[0] // val[1]
            if avg > res_avg_score:
                res_avg_score = avg
                res_name = key
        return res_name, res_avg_score

s = Solution()
scores = [["Bob", "90"], ["John", "82"], ["Bob", "96"],["Bob", "94"],["John", "78"], ["me", "72"]]
scores = [("Bob","87"), ("Mike", "35"),("Bob", "52"), ("Jason","35"), ("Mike", "55"), ("Jessica", "99")]
a, b = s.find_maxavg(scores)
print(a)
print(b)

"""     
s = Solution()
scores = [("Bob","87"), ("Mike", "35"),("Bob", "52"), ("Jason","35"), ("Mike", "55"), ("Jessica", "99")]
print(s.maxAvgScore(scores))
"""