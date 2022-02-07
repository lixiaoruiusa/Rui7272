"""
一串‍‍‌‌‌‌‌‌‍‍‍‌‌‍‍‌‍‍‌‌数字，如果必须移掉一个'5'，产生的最大数字是多少
第三题 我觉的是找规律，如果是正数，只要5后面的数字比5大，移除了5之后的数肯定大于不移除的。

所以只需要找第一个 5小于后面数字，然后移除。
针对负数，先取正，再找第一个 5大于后面数的位置移除。
找不到，就移除最后一个5.
"""
# n**2??

n = 5163435
removed = 5

def helper(n, removed):
    array = list(str(n))
    is_remove = False
    last_removed_index = -1
    for i in range(len(array) - 1):
        # tracking the last target may be removed
        if int(array[i]) == removed:
            last_removed_index = i
        # 找第一个5小于后面数字，然后移除
        if int(array[i]) == removed and int(array[i + 1]) > removed:
            array.pop(i)
            is_remove = True
            return array
    if array[-1] == removed
    print(last_removed_index,array)
    # not found
    if last_removed_index == -1:
        return -1
    # all 5 behind is small, the remove last 5
    if is_remove == False:
        array.pop(last_removed_index)
    return array

print(helper(n,removed))