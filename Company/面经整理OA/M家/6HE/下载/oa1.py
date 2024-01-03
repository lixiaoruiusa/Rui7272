# LeetCode 1822
# https://leetcode.com/problems/sign-of-the-product-of-an-array/
def arraySign(nums: list[int]) -> int:
    neg = 0
    for num in nums:
        if num == 0:
            return 0
        elif num < 0:
            neg += 1
    return 1 if neg % 2 == 0 else -1

print(arraySign([-1,-1,-1,-1,1,-1]))
print(arraySign([-1,-1,0,-1,1,-1]))
print(arraySign([-1,-1,1]))