'''
Time complexity: O(4^n * N) where N is the length of digits.
(4^n is because 9797 的树形 recurtion
 N is because list to string ''.join(chars))
Space complexity: O(N), where N is the length of digits.

题意： 类似于拨电话号码，求所有输出的组合
思路： dfs 传入combination， combinations， index， loop and backtrack “abc”
'''
dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
       "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = []
        self.dfs(digits, 0, [], combinations)
        return combinations

    def dfs(self, digits, index, combination, combinations):
        if index == len(digits):
            combinations.append("".join(combination))
            return

        for letter in dic[digits[index]]:
            combination.append(letter)
            self.dfs(digits, index + 1, combination, combinations)
            combination.pop()