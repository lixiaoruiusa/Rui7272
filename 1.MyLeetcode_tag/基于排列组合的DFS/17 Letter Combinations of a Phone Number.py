'''
Time complexity: O(4^n * N) where N is the length of digits.
(4^n is because 9797 的树形 recursion
 N is because list to string ''.join(chars))

Space complexity: O(N), where N is the length of digits.

题意： 类似于拨电话号码，求所有输出的组合
思路： dfs 传入combination， combinations， index， loop and backtrack “abc”
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        results = []
        self.dfs(digits, results, [], 0)
        return results

    def dfs(self, digits, results, path, index):

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if index == len(digits):
            results.append("".join(path))
            return

        for letter in letters[digits[index]]:
            path.append(letter)
            self.dfs(digits, results, path, index + 1)
            path.pop()