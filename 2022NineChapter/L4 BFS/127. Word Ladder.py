import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        wordList.add(beginWord)
        queue = collections.deque([beginWord])
        visited = set([beginWord])

        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance

                for next_word in self.get_next_words(word):
                    if next_word not in wordList or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
        return 0

    # O(26 * L^2)
    # L is the length of word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words









