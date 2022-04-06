class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # Time complexity: O(M), where M is the key length.
    # Space complexity: O(M) create node

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    # Time complexity: O(M) where M is the key length.
    # Space complexity: O(1)
    def search(self, word: str) -> bool:
        if not word:
            return False

        cur = self.root
        return self.dfs(word, cur, 0)

    def dfs(self, word, cur, index):

        if len(word) == index:
            return cur.is_word

        c = word[index]

        if c != '.':
            if c not in cur.children:
                return False
            else:
                return self.dfs(word, cur.children[c], index + 1)
        else:
            for key in cur.children:
                if self.dfs(word, cur.children[key], index + 1):
                    return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)