def maxDepthString(s: str) -> list:
    max_depth = 0
    output = []
    open_brackets = {"(": ")", "{": "}", "[": "]"}
    closing_brackets = {")", "}", "]"}

    left = 0
    curr_depth = 0
    for right, c in enumerate(s):
        if c in open_brackets:
            left = right
            curr_depth += 1
            if curr_depth > max_depth:
                max_depth = curr_depth
                #output = []

        if c in closing_brackets and c == open_brackets[s[left]]:
            output.append(s[left + 1: right])
            curr_depth -= 1

    return output


print(maxDepthString("abc(def)ghi") == ["def"])
print(maxDepthString("abc(def[ghi]jkl)mno") == ["ghi"])
print(maxDepthString("abc(def)ghi[jkl]mno") == ["def", "jkl"])
print(maxDepthString("abc") == [])
print(maxDepthString("([{a}{b}]c)") == ["a", "b"])
print(maxDepthString("abc(def)g[hi]") == ["def", "hi"])