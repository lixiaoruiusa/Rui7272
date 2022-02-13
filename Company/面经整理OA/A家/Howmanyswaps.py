a = [5, 1, 4, 2]

def swap(array):
    if not array:
        return 0

    i = 0
    j = 1
    n = len(array)
    count = 0

    while i < len(array):
        while j < n and array[i] < array[j]:
            j += 1

        if j >= n:
            i += 1
            j = i + 1
            continue

        array[i], array[j] = array[j], array[i]
        count += 1
        j += 1
        print(array)
        continue

    print(count)

swap(a)