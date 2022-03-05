# 题意： 给n个人，检查里边有没有名人。名人就是只认识自己，不认识别人，看看存不存在一个这样的人
# 思路：candidate = 0，一个loop选出candidate，一个loop检查candidate。
# 筛选候选人: 因为这个名人不认识其他人，所以candidate = i就是潜在的名人，妙啊~~
# 检查候选人：只认识自己，不认识别人，别人都认识他
# graph[i][j] = 1 代表编号为 i 的人认识编号为 j 的人，而 graph[i][j] = 0 则代表编号为 i 的人不认识编号为 j 的人
# 所以名人的条件是列都是1，行都为0，除了自己
# Time Complexity : O(n)
# Space Complexity : O(1)
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        for i in range(n):
            if i == candidate:
                continue
            if not knows(i, candidate):
                return -1
            if knows(candidate, i):
                return -1
        return candidate


"""
# APP4: Follow up: what to do if the call is really expensive?
# Even APP3 is O(n), there're still duplicated calls in the second pass
# We can cache the result in a hashmap
# Time: O(n), space: O(n)
# 也就稍微省了几个call吧
    def findCelebrity(self, n):
        if not n or n < 0:
            return -1 
        celeb = 0
        memo = {}   # x know y , T or F
        for i in range(1, n):
            if Celebrity.knows(celeb, i):
                memo[(celeb, i)] = True
                celeb = i
            else:
                memo[(celeb, i)] = False
        return self.is_celeb(celeb, n, memo)
        
    def is_celeb(self, celeb, n, memo):
        for i in range(n):
            if celeb == i:
                continue
            if (celeb, i) in memo and memo[(celeb, i)]:  # candidate认识了一个人gg
                return -1
            if (i, celeb) in memo and not memo[(i, celeb)]: # 有一个人不认识candidate也gg
                return -1
            if Celebrity.knows(celeb, i) or not Celebrity.knows(i, celeb):
                return -1 
        return celeb
"""