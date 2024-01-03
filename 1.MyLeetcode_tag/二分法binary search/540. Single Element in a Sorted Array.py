class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if (right - mid) % 2 == 0:
                right_are_even = True
            else:
                right_are_even = False
            # 和右边相等, 右边是偶数，证明实际是奇数with mid
            if nums[mid + 1] == nums[mid]:
                if right_are_even:
                    left = mid + 2
                else:
                    right = mid - 1
            # 和左边相等, 右边是偶数，证明实际是奇数with mid
            elif nums[mid - 1] == nums[mid]:
                if right_are_even:
                    right = mid - 2
                else:
                    left = mid + 1
            # 左右都不相等
            else:
                return nums[mid]

        # left 和 right 都落到single的位置
        return nums[left]