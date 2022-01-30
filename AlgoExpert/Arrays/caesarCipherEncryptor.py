def caesarCipherEncryptor(string, key):
    result = []
    newKey = key % 26

    for letter in string:
        newLetter = ord(letter) + newKey
        if newLetter <= 122:
            result.append(chr(newLetter))
        else:
            result.append(chr(96 + newLetter % 122))

    return "".join(result)