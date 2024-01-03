"""
3. Given a string s, find the minimum number of substrings you can create without having the same letters repeating in each substring.
E.‍‍‌‌‌‌‌‌‍‍‍‌‌‍‍‌‍‍‌‌g world -> 1, as the string has no letters that occur more than once.
dddd -> 4, as you can only create substring of each character.
abba -> 2, as you can make substrings of ab, ba.
cycle-> 2, you can create substrings of (cy, cle) or (c, ycle)

"""
s1 = "dddd"
s2 = "abba"
s3 = "cycle"


def find_min_number(s):
    if not s:
        return 0
    validate = set()
    count = 1
    for ch in s:
        if ch in validate:
            count += 1
            validate.clear()
        validate.add(ch)
    return count
