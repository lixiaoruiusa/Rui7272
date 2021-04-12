def isValidSubsequence(array, sequence):
    # Write your code here.
    index_seq = 0
    for num in array:
        if index_seq < len(sequence) and num == sequence[index_seq]:
            index_seq += 1

    return index_seq == len(sequence)


def isValidSubsequence(array, sequence):
    index_seq = 0
    for num in array:
        if index_seq == len(sequence):
            break
        if num == sequence[index_seq]:
            index_seq += 1

    return index_seq == len(sequence)