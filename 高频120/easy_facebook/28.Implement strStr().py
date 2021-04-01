class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    @Time: O(n^2) Space: O(1)
    """
    def strStr(self, source, target):
        if target is None:
            return 0
        if source is None:
            return -1
        if source == target:
            return 0
        len_source = len(source)
        len_target = len(target)
        
        for i in range(len_source - len_target + 1):
            if source[i:i+len_target] == target:
                return i
        else:
            return -1

 '''
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        if not haystack:
            return -1

        for i in range(len(haystack)):
            if needle == haystack[i: i + len(needle)]:
                return i

        return -1
'''
