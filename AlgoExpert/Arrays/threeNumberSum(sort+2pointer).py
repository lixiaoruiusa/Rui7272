# Time complexity: O(nlogn + n^2)
# Space complexity: O(1)

def threeNumberSum(array, targetSum):
    # Write your code here.
    if not array or len(array) < 3:
        return []
    res = []
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current = array[i] + array[left] + array[right]
            if current == targetSum:
                res.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current > targetSum:
                right -= 1
            else:
                left += 1

    return res
