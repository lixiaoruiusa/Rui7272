def generateDocument(characters, document):
    dic = {}

    for ch in characters:
        if ch not in dic:
            dic[ch] = 1
        else:
            dic[ch] += 1

    for word in document:
        if word not in dic or dic[word] == 0:
            return False
        else:
            dic[word] -= 1

    return True
