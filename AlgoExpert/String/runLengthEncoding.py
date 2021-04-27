# O(n)time | O(n) space
# count from index 1, length = 1; if not add to res; handle last case

def runLengthEncoding(string):
    res = []
    length = 1

    for i in range(1, len(string)):
        if string[i] != string[i - 1] or length == 9:
            res.append(str(length))
            res.append(string[i - 1])
            length = 1
        else:
            length += 1

    # handle the last run
    res.append(str(length))
    res.append(string[len(string) - 1])

    return "".join(res)
