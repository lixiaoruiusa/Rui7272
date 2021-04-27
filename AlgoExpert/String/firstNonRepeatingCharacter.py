# O(n) time | O(1) space
def firstNonRepeatingCharacter(string):
    dic = {}

    for ch in string:
        if ch not in dic:
            dic[ch] = 1
        else:
            dic[ch] += 1
    for i in range(len(string)):
        if dic[string[i]] == 1:
            return i

    return -1
