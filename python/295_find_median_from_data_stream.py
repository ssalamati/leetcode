class MedianFinder:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def addNum(self, num: int) -> None:
        if not self.min_heap or num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        while len(self.min_heap) - len(self.max_heap) >= 2:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        while len(self.max_heap) - len(self.min_heap) >= 2:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        

    def findMedian(self) -> float:
        if len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()