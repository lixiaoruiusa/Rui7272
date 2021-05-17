# O(n) Time | O(n) space
# 1 key 要 % 26
# 2 helper 里 每个元素 ord + key
# return <= 122 的值
# ord是unicode ordinal的缩写，即编号；
# chr是character的缩写，即缩写
# ord和chr是互相对应转换的.


def caesarCipherEncryptor(string, key):
    res = []
    new_key = key % 26

    for letter in string:
        res.append(get_new_letter(letter, new_key))

    return "".join(res)


def get_new_letter(letter, key):
    new_letter_code = ord(letter) + key

    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)
