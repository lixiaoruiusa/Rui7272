class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        res = []
        for q in queries:
            t = self.is_match(q, pattern)
            res.append(t)
        return res

        # 指针匹配，分析queris中的每个字符会被如何使用
        # 当它是大写字符的时候，尝试匹配pattern,必须匹配
        # 当它是小写字符的时候，尝试匹配pattern,可能匹配

    def is_match(self, q, pattern):
        n1 = len(q)
        n2 = len(pattern)
        i = 0
        j = 0
        # while匹配q
        while i < n1:
            if q[i].upper() == q[i]:  # 大写
                if j < n2 and q[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    return False
            elif q[i].lower() == q[i]:  # 小写
                if j < n2 and q[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
        return j == n2