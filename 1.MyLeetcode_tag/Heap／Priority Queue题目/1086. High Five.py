# 题意：给了所有学生的（id score）返回所有人的[id, top5平均分]，并按照id排序
# 思路：1 建一个 {student_id: [top-5 scores]} 字典, 用min_heap维持 dic[student_id] 最多5个。
#      2 把id和平均分加入res
#      3 最后要sort res
# Time: O(Nlogk) 我觉得是nlogk
# Space: O(N)

import heapq


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # cache = defaultdict(list)  # {student_id: [top-5 scores]}
        dic = {}
        for student_id, score in items:
            if student_id not in dic:
                dic[student_id] = [score]
            else:
                heapq.heappush(dic[student_id], score)
                if len(dic[student_id]) > 5:
                    heapq.heappop(dic[student_id])

        res = []
        for student_id, scores in dic.items():
            average = sum(scores) // len(scores)
            res.append([student_id, average])

        res.sort()
        return res