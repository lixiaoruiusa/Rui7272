"""
从 end 到 start 做一次 BFS，并且把距离 end 的距离都保存在 distance 中。 然后在从 start 到 end 做一次 DFS，每走一步必须确保离 end 的 distance 越来越近。

Time complexity: O(NK^2 + α)
N is the number of words in wordList,K is the maximum length of a word, α is the number of possible paths from beginWord to endWord in the directed graph we have.

Space complexity: O(NK).
N is the Number of words in wordList, K is the Maximum length of a word.
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordList = set(wordList)
        wordList.add(beginWord)

        distance = {}
        self.bfs(endWord, distance, wordList)

        results = []
        self.dfs(beginWord, endWord, distance, wordList, [beginWord], results)

        return results


    def bfs(self, beginWord, distance, wordList):
        distance[beginWord] = 0
        queue = deque([beginWord])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, wordList):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)


    # def bfs(self, beginWord, distance, wordList):
    #     dis = 0
    #     distance[beginWord] = 0
    #     queue = deque([beginWord])
    #     while queue:
    #         dis += 1
    #         for i in range(len(queue)):
    #             word = queue.popleft()
    #             for next_word in self.get_next_words(word, wordList):
    #                 if next_word not in distance:
    #                     distance[next_word] = dis
    #                     queue.append(next_word)

    def get_next_words(self, word, wordList):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in wordList:
                    words.append(next_word)
        return words

    # self.dfs(beginWord, endWord, distance, wordList, [beginWord], results)
    # {'cog': 0, 'dog': 1, 'log': 1, 'dot': 2, 'lot': 2, 'hot': 3, 'hit': 4}
    def dfs(self, cur, endWord, distance, wordList, path, results):
        if cur == endWord:
            results.append(list(path))
            return

        for word in self.get_next_words(cur, wordList):

            if distance[word] != distance[cur] - 1:
                continue
            path.append(word)
            self.dfs(word, endWord, distance, wordList, path, results)
            a = path.pop()

