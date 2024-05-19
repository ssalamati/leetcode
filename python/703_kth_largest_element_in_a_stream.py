class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.meanheap, self.k = nums, k
        heapq.heapify(self.meanheap)

        while len(self.meanheap) > k:
            heapq.heappop(self.meanheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.meanheap, val)

        if len(self.meanheap) > self.k:
            heapq.heappop(self.meanheap)

        return self.meanheap[0]
