
s = 'acbbbccddd'

def remove_triple(s):
    finished = True
    i = len(s) - 1
    while i >= 2:
        if s[i] == s[i - 1] == s[i - 2]:
            s = s[:i - 2] + s[i + 1:]
            i = i - 3
            finished = False
        i -= 1
    if finished:
        return s
    else:
        return remove_triple(s)


a = remove_triple(s)
print(a)