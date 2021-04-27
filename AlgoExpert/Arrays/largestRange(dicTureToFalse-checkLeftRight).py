# O(n) time | O(n) space
def largestRange(array):
    if not array:
        return
    array = list(set(array))
    dic = {}
    best = []
    longest_length = 0

    for num in array:
        dic[num] = True

    for num in array:
        if not dic[num]:
            continue
        dic[num] = False
        current_length = 1
        left = num - 1
        right = num + 1

        while left in dic:
            dic[left] = False
            current_length += 1
            left -= 1

        while right in dic:
            dic[right] = False
            current_length += 1
            right += 1

        if current_length > longest_length:
            longest_length = current_length
            best = [left + 1, right - 1]

    return best