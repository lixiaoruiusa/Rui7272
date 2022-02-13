"""
一串‍‍‌‌‌‌‌‌‍‍‍‌‌‍‍‌‍‍‌‌数字，如果必须移掉一个'5'，产生的最大数字是多少
第三题 我觉的是找规律，如果是正数，只要5后面的数字比5大，移除了5之后的数肯定大于不移除的。

所以只需要找第一个 5小于后面数字，然后移除。
针对负数，先取正，再找第一个 5大于后面数的位置移除。
找不到，就移除最后一个5.
"""


"""
Convert to String type
Check whether it contains 5 or not?
If length of digit is less than two return same number
Now search for all the indices in string whether character is 5
Now remove 5 for each index one by one and store the resultant digits into possibilities
Return maximum number from all possibilities
"""

# Time O(n**2) n is length of string | Space O(n)
def solution(n, digit):
    possibles = []
    # indexes of 5
    to_remove_index = []
    n = str(n)
    if "5" not in n:
        return -1
    elif len(n) < 2:
        return -1
    for i in range(len(n)):
        if str(n[i]) == str(digit):
            to_remove_index.append(i)

    for k in to_remove_index:
        chars = list(n)
        chars[k] = ''
        possibles.append(int("".join(chars)))
    return max(possibles)

#print(solution(5163435, 5))

"""

def solution(N):
    if type(N) != int:
        N = int(N)
    # all_possibles numbers
    possibles = []
    # indexes of 5
    fives = []
    N = str(N)
    if "5" not in N:
        print("There must be atleast one 5")
        return int(N)
    elif len(N) < 2:
        print("Must be atleast 2 digit Number")
        return int(N)
    for i in range(0, len(N)):
        if str(N)[i] == "5":
            fives.append(i)
    print("5 found on indices = ", fives)
    for k in fives:
        chars = list(N)
        chars[k] = ''
        print("Replace {} 5 in {} and get {}".format(k, N, int("".join(chars))))
        possibles.append(int("".join(chars)))
    print("all combos = ", possibles)
    return max(possibles)
"""




# n**2??
#
# n = 5163435
# removed = 5
#
# def helper(n, removed):
#     array = list(str(n))
#     is_remove = False
#     last_removed_index = -1
#     for i in range(len(array) - 1):
#         # tracking the last target may be removed
#         if int(array[i]) == removed:
#             last_removed_index = i
#         # 找第一个5小于后面数字，然后移除
#         if int(array[i]) == removed and int(array[i + 1]) > removed:
#             array.pop(i)
#             is_remove = True
#             return array
#     if array[-1] == removed
#     print(last_removed_index,array)
#     # not found
#     if last_removed_index == -1:
#         return -1
#     # all 5 behind is small, the remove last 5
#     if is_remove == False:
#         array.pop(last_removed_index)
#     return array
#
# print(helper(n,removed))
#