# O(1) Time | O(1) Space
# check 4 part: string[:i+1], string[i+1:j+1], string[j+1:k+1], string[k+1:]

def validIPAddresses(string):
    validIPAddresses = []

    if not string or len(string) < 4:
        return []

    for i in range(3):
        # check first dot
        if not isValidPart(string[:i + 1]):
            continue
        # check second dot
        for j in range(i + 1, i + 4):
            if not isValidPart(string[i + 1:j + 1]):
                continue
            # check third dot
            for k in range(j + 1, j + 4):
                if not isValidPart(string[j + 1:k + 1]) or not isValidPart(string[k + 1:]):
                    continue

                validIP = string[:i + 1] + "." + string[i + 1:j + 1] + "." + string[j + 1:k + 1] + "." + string[k + 1:]
                validIPAddresses.append(validIP)
    return validIPAddresses


def isValidPart(string):
    if len(string) == 1:
        return True

    if not 0 < len(string) < 4 or string[0] == "0":
        return False

    if 0 <= int(string) <= 255:
        return True

    return False