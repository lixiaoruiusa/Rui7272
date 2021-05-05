
s = 'abcdecbbbccddd'
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




def candy_crush(input):
    if not input:
        return input

    stack = []
    stack.append([input[0], 1])


    for i in range(1, len(input)):
        print(stack)
        if input[i] != input[i - 1]:
            if stack[-1][1] >= 3:
                stack.pop()
            if stack and stack[-1][0] == input[i]:
                stack[-1][1] += 1
            else:
                stack.append([input[i], 1])
        else:
            stack[-1][1] += 1

    # handle end
    if stack[-1][1] >= 3:
        stack.pop()

    out = []
    for ltrs in stack:
        out += ltrs[0] * ltrs[1]

    return ''.join(out)


candy_crush("aaaabbbc")

# print(candy_crush("aaaabbbc"))  # c
# print(candy_crush("aabbbacd"))  # cd
# print(candy_crush("aabbccddeeedcba"))  # blank expected
# print(candy_crush("aabbbaacd"))  # cd
# print(candy_crush("dddabbbbaccccaax"))  # x