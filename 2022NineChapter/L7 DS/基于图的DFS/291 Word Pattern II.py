class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        if not pattern and not s:
            return True
        if not pattern or not s:
            return False

        dic = {}
        visited = set()
        return self.is_match(pattern, s, dic, visited)

    def is_match(self, pattern, s, dic, visited):

        #  当pattern搜索到末尾且str也搜索到末尾即能完全匹配，返回true
        if len(pattern) == 0:
            return len(s) == 0

        # 如果当前模板的字母已经有匹配过字符串word
        ch = pattern[0]
        if ch in dic:
            word = dic[ch]
            if not s.startswith(word):
                return False
            # 如果这个word能匹配上，就进行后边的匹配
            if self.is_match(pattern[1:], s[len(word):], dic, visited):
                return True
            else:
                return False

        # 如果当前模板的字母未匹配过字符串：
        for i in range(len(s)):
            word = s[:i + 1]
            if word in visited:
                continue

            dic[ch] = word
            visited.add(word)
            if self.is_match(pattern[1:], s[i + 1:], dic, visited):
                return True
            visited.remove(word)
            del dic[ch]

        return False


