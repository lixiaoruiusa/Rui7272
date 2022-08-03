"""
间复杂度：O(m×n×4^l)
其中m是二维网格的高度，n是二维网格的宽度，l 是最长单词的长度。

空间复杂度：O(k×l)，
其中 k是words长度，l是最长单词的长度。用于存储前缀树
"""

"""
root
{c1: TrieNode(),   c2, c3}
      {cc1: TrieNode()}


"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for word in words:
            trie.insert(word)
        visited = [[False for col in range(len(board[0]))] for row in range(len(board))]
        results = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.children:
                    visited[i][j] = True
                    self.dfs(board, trie.root.children[board[i][j]], i, j, visited, results)
                    visited[i][j] = False
        return results

    def dfs(self, board, root, i, j, visited, results):
        # 当dfs到是一个word，而且不在results里时，加入结果。
        if root.word != "" and root.word not in results:
            results.append(root.word)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = dx + i, dy + j
            if not (0 <= x < len(board) and 0 <= y < len(board[0]) and not visited[x][y]):
                continue
            if board[x][y] not in root.children:
                continue
            visited[x][y] = True
            self.dfs(board, root.children[board[x][y]], x, y, visited, results)
            visited[x][y] = False

