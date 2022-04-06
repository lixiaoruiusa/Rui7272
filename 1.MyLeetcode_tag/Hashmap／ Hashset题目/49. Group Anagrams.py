# 注意的是字典里存的为{'aet': ['eat']}，else的结果要append
# Time O(n * klogk) N is the length of strs, K is the maximum length of a string in strs
# Space O(nk)  the total information content stored in ans
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        results = []
        dic = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)
        return dic.values()

        # for result in dic.values():
        #     results.append(result)
        # return results


