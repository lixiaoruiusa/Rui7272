def balancedBrackets(string):
    if not string: return True

    stack = []
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchBracket = {")": "(", "]": "[", "}": "{"}
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if not stack:
                return False
            if matchBracket[char] != stack[-1]:
                return False
            stack.pop()

    return not stack

