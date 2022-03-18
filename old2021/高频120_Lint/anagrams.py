class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    @ Time complexity: O(n) or nlog(n)??  Space complexity: O(n)
    """
    def anagrams(self, strs):
        # write your code here
        dict = {}
        res = []
        
        for word in strs:
            # sort word
            sortedword = ''.join(sorted(word))
            # 放入字典key为sortedword， value为[word] 
            # {'ilnt': ['lint', 'intl', 'inlt'], 'cdeo': ['code']}
            if sortedword not in dict:
                dict[sortedword] = [word]
            else:
                dict[sortedword] = dict[sortedword] + [word]
        # 取出字典内vlaue大于1的value， add 到 res
        for item in dict:
            if len(dict[item]) >=2:
                # 因为value是[], 所以 +
                res += dict[item]
            
        return res
