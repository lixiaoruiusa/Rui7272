"""
时间复杂度：O(L^2 * N)
N为dict中单词个数，s代表字符集大小(这题中是26)，m为单词长度。因为bfs所有节点最多遍历一次，每次遍历到之后，需要扫遍单词的每个字符，每个字符均可以变化为其他25个不同字母

空间复杂度：O(NL)
N为dict中单词个数，L为单词长度。用于bfs的队列最大需存下所有节点。
set and q all is O(NL)
建立每个word可能需要 N * L^2 space ?
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if not beginWord or not endWord:
            return 0
        if beginWord == endWord:
            return 1

        wordList = set(wordList)
        distance = 0
        visited = set()
        q = collections.deque()
        q.append(beginWord)
        visited.add(beginWord)

        while q:
            distance += 1
            for i in range(len(q)):
                cur = q.popleft()
                if endWord == cur:
                    return distance
                else:
                    for next_word in self.get_next_word(cur, wordList, visited):
                        q.append(next_word)
                        visited.add(next_word)
        return 0


    def get_next_word(self, word, wordList, visited):
        res = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i + 1:]
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch != word[i]:
                    new_word = left + ch + right
                    if new_word in wordList and new_word not in visited:
                        res.append(new_word)
        return res


    # def get_next(self, cur_word, dic):
    #     next_words = []
    #     for next_word in dic:
    #         diff_count = 0
    #         for i in range(len(cur_word)):
    #             if cur_word[i] != next_word[i]:
    #                 diff_count += 1
    #         if diff_count == 1:
    #             next_words.append(next_word)
    #     return next_words
