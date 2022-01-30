# O(N**2) Time and O(N) Space
# 1 sortStack(pop all, the insert) 2 insertStack
def sortStack(stack):
    if not stack:
        return stack

    top = stack.pop()
    sortStack(stack)
    insertStack(stack, top)
    return stack


def insertStack(stack, value):
    if not stack or stack[len(stack) - 1] <= value:
        stack.append(value)
        return

    top = stack.pop()
    insertStack(stack, value)
    stack.append(top)

