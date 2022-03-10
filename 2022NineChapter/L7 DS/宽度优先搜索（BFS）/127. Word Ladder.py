# Time Complexity: O(M^2 N), where M is the length of each word and N is the total number of words in the input word list.
# Space Complexity:
# O (nm) n为dict中单词个数，m为单词长度。用于bfs的队列最大需存下所有节点。
# Visited dictionary would need a space of O(M×N) as each word is of length M.
# Queue for BFS in worst case would need a space for all O(N) words and this would also result in a space complexity O(M×N)

import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        if not beginWord or not endWord:
            return 0

        wordList = set(wordList)
        wordList.add(beginWord)

        visited = set()
        queue = collections.deque([beginWord])
        visited.add(beginWord)

        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                cur_word = queue.popleft()
                if cur_word == endWord:
                    return distance
                # get next word
                next_words = self.get_next_words(cur_word, wordList)
                for next_word in next_words:
                    if next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)
        return 0

    def get_next_words(self, cur_word, wordList):
        next_words = []
        for i in range(len(cur_word)):
            left = cur_word[:i]
            right = cur_word[i + 1:]
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c != cur_word[i]:
                    new_word = left + c + right
                    if new_word in wordList:
                        next_words.append(new_word)
        return next_words

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