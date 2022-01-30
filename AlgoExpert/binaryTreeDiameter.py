# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    diameter = [0]
    dfs(tree, diameter)
    return diameter[0]


def dfs(tree, diameter):
    if tree is None:
        return 0

    left = dfs(tree.left, diameter)
    right = dfs(tree.right, diameter)

    diameter[0] = max(diameter[0], left + right)
    return max(left, right) + 1
