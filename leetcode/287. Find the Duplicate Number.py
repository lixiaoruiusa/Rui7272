class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

#         slow = fast = finder = 0
#         slow = nums[slow]
#         fast = nums[nums[fast]]

#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[nums[fast]]


#         while finder != slow:
#             finder = nums[finder]
#             slow = nums[slow]
#         return finder


# slow = fast = finder = 0
# while True:
#     slow = nums[slow]
#     fast = nums[nums[fast]]
#     if slow == fast:
#         while finder != slow:
#             finder = nums[finder]
#             slow = nums[slow]
#         return finder

'''
[1,3,4,2,2]
什么是快慢指针算法？ 从起点出发，慢指针走一步，快指针走两步。因为有环，所以一定会相遇。
相遇之后，把其中一根指针拉回起点，重新走，这回快慢指针都各走一步。
他们仍然会再次相遇，且相遇点为环的入口。

'''
