def twoNumberSum(array, targetSum):
    # Write your code here.

    dic = {}

    for i in range(len(array)):
        if targetSum - array[i] in dic:
            return [array[i], targetSum - array[i]]
        else:
            dic[array[i]] = i

    return []