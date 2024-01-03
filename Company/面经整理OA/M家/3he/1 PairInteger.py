"""
给一个int数组，问你里面所有的元素是否能配对(相同的两个元素可以配成一对)。
[1,2,2,1]: true, [7,7,7]: false, [1,2,2,3]: false
"""

array = []
def find_pair(array):

    if not array:
        return
    new_set = set()
    for num in array:
        if num not in new_set:
            new_set.add(num)
        else:
            new_set.remove(num)
    return len(new_set) == 0




# create a set to store the numbers.
# iterate the list: if element not in set, then add element. if element is in set, then remove from set.
# at last, if set is empty which means all elements paired.
# O(n) time where n is the length of input list and O(n) space is the worse case of all elements are unique.


array = [0,0,0]
def find_pair2(array):

    if not array:
        return
    res = 0
    for a in array:
        res = res ^ a
        print(res)
    return res == 0

print(find_pair2(array))