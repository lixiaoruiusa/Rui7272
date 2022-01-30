# MINIMUM CHARACTERS FOR WORDS

# O(N * L) time, N - no of words, L - length of longest word
# O(C) space - lower bound, C - no of unique characters
# o(N * L) space - upper bound, since there might be words having all same characters
# eg {"a": 3"} with one character but an output array ["a", "a", "a"] with three characters


def minimumCharactersForWords(words):
    result = {}

    for word in words:
        temp = {}
        for letter in word:
            if letter not in temp:
                temp[letter] = 1
            else:
                temp[letter] += 1

            if letter not in result or result[letter] < temp[letter]:
                result[letter] = temp[letter]

    outPut = []
    for letter in result:
        for freq in range(result[letter]):
            outPut.append(letter)

    return outPut

