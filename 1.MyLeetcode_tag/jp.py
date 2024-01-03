
#input as array
nums =  [(1,100),(2, 200),(3, 300)]
res = []
left = 0
for right in range(len(nums)):

    if right - left == 15:
        res.append(nums[right] - nums[left])

res = []