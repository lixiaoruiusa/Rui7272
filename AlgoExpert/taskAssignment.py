# O(nlogn) time | O(n) space

def taskAssignment(k, tasks):
    if not tasks or len(tasks) < 2: return []

    dictionary = {}
    result = []
    for i in range(len(tasks)):
        if tasks[i] not in dictionary:
            dictionary[tasks[i]] = [i]
        else:
            dictionary[tasks[i]].append(i)

    sortedTasks = sorted(tasks)

    for idx in range(k):
        task1 = sortedTasks[idx]
        firstIdx = dictionary[task1].pop()
        task2 = sortedTasks[len(sortedTasks) - 1 - idx]
        secondIdx = dictionary[task2].pop()
        result.append([firstIdx, secondIdx])
    return result






