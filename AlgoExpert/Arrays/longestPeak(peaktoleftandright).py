def longestPeak(array):
    res = 0

    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peak = left = right = i

            while left > 0 and array[left] > array[left - 1]:
                left -= 1
            while right < len(array) - 1 and array[right] > array[right + 1]:
                right += 1

            res = max(res, right - left + 1)

    return res

