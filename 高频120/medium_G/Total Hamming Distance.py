class Solution:
    """
    @param nums: the gievn integers
    @return: the total Hamming distance between all pairs of the given numbers
    @ Time O(32*n) ~= O(n)
    @ for i in range(32):
        mask = 1 << i
        print(i)
        print("{0:b}".format(mask))
    """

    def totalHammingDistance(self, nums):
        # Write your code here
        ans = 0

        for i in range(32):
            zero = one = 0
            mask = 1 << i
            for num in nums:
                if mask & num:
                    one += 1
                else:
                    zero += 1
            ans += one * zero
        return ans