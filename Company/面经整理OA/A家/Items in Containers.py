'''
Given a string s consisting of items as "*" and closed compartments as an open and close "|", an array of starting indices startIndices, and an array of ending indices endIndices, determine the number of items in closed compartments within the substring between the two indices, inclusive.

An item is represented as an asterisk *
A compartment is represented as a pair of pipes | that may or may not have items between them.
Example:
s = '|**|*|*'
startIndices = [1,1]
endIndices = [5,6]

The String has a total 2 closed compartments, one with 2 items and one with 1 item. For the first par of indices, (1,5), the substring is '|**|*'. There are 2 items in a compartment.
For the second pair of indices, (1,6), the substring is '|**|*|' and there 2+1=3 items in compartments.
Both of the answers are returned in an array. [2,3].
'''


s = '|**|*|*'
s1 = s.split()
s2 = list(s)
# print(s1)
# print(s2)


startIndices = [1,1]
endIndices = [5,6]


def numbers_of_items(s,startIndices,endIndices):
    if not s:
        return 0

    mem = [0] * len(s)
    count = 0
    lists = list(s)

    for i in range(len(lists)):
        if lists[i] == "|":
            mem[i] = count
        else:
            count += 1
    print(mem)

    result = []
    for i in range(len(startIndices)):
        startIndex = startIndices[i] - 1
        endIndex = endIndices[i] - 1

        while lists[startIndex] != "|":
            startIndex += 1
        while lists[endIndex] != "|":
            endIndex -= 1

        print(startIndex,endIndex)
        result.append(mem[endIndex] - mem[startIndex])

    print(result)
    return result


numbers_of_items(s,startIndices,endIndices)











