"""
The amazon question is given an array of only 1s and 0s where you can only make adjacent swaps, return the min number of swaps required to have all 1s or 0s on one side.
Eg. [0, 1, 0, 1] would return 1 since it takes 1 swap to have it as [0, 0, 1, 1] which is the minimum.
[1, 1, 0, 0] would be a valid array except it is not in the minimum as it would take 3 swaps.
"""
nums = [1,4,5,2]
nums = sorted(nums, reverse = True)
print(nums)