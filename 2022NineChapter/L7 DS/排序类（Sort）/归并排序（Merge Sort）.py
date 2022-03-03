# nlogn time | nlogn space
def mergeSort(array):
    if not array or len(array) < 2:
        return array

    mid = len(array) // 2
    left_array = mergeSort(array[:mid])
    right_array = mergeSort(array[mid:])
    print(mid, left_array,right_array)
    return merge(left_array, right_array)


def merge(left_array, right_array):
    #print(left_array, right_array)
    result = []
    i = 0
    j = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1

    # 将剩余的元素合并到新的列表中
    result += left_array[i:]
    result += right_array[j:]

    return result

mergeSort([4,3,2,1])