# O(w * nlogn) Time | O(wn) Space
# w is number of words; n is max length of word
def groupAnagrams(words):
    dic = {}

    for word in words:
        sorted_word = ''.join(sorted(word))

        if sorted_word in dic:
            dic[sorted_word].append(word)
        else:
            dic[sorted_word] = [word]

    res = list(dic.values())

    return res
