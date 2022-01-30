# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

#(N) time and (N) space

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    visited = set()
    while descendantOne != topAncestor:
        visited.add(descendantOne)
        descendantOne = descendantOne.ancestor

    while descendantTwo != topAncestor:
        if descendantTwo in visited:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor

    return topAncestor

