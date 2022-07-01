def longestSubstringWithoutDuplication(string):
    if not string:
        return ""

    res = ""
    longest = 0

    dic = {}
    left = 0
    for right in range(len(string)):
        dic[string[right]] = dic.get(string[right], 0) + 1

        while dic[string[right]] > 1:
            dic[string[left]] -= 1
            left += 1

        if right - left + 1 > longest:
            longest = right - left + 1
            res = string[left: right + 1]
    return res