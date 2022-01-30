'''
Time complexity: O(4^n * N) where N is the length of digits.
(4^n is because 9797 的树形 recurtion
 N is because list to string ''.join(chars))
Space complexity: O(N), where N is the length of digits.
'''


def phoneNumberMnemonics(phoneNumber):
    if not phoneNumber:
        return []
    results = []
    dfs(phoneNumber, 0, [], results)
    return results


def dfs(phoneNumber, index, chars, results):
    print(1)
    if index == len(phoneNumber):
        results.append("".join(chars))
        return

    for letter in KEYBOARD[phoneNumber[index]]:
        chars.append(letter)
        dfs(phoneNumber, index + 1, chars, results)
        chars.pop()


KEYBOARD = {
    "0": "0",
    "1": "1",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"}