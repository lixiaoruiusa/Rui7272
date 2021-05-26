class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # if heap grows bigger then k remove elements

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# init nlogn time  # build 是 O(n)| space n
# add logk time | space k space
# O(n) time for buildHeap and O(n log n) to remove each node in order, so the complexity is O(n log n)