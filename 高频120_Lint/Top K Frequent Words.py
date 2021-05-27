class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    @ MinHeap NlogK， O（n）
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        if not words or not k:
            return []
        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        
        from heapq import heappush, heappop
        heap = []
        for word in d:
            heappush(heap, (-d[word], word))
        
        ans = []
        for i in range(k):
            num, word = heappop(heap)
            ans.append(word)
            
        return ans
        
        
        
