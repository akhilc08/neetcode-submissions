class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num: int) -> None:
        
        if self.minheap and num>self.minheap[0]: 
            heapq.heappush(self.minheap, num)
        else: 
            heapq.heappush(self.maxheap, -num)

        while len(self.maxheap) - len(self.minheap) > 1: 
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        while len(self.minheap) - len(self.maxheap) > 1: 
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            
    def findMedian(self) -> float:

        if not self.maxheap: return self.minheap[0]
        if not self.minheap: return -self.maxheap[0]

        if len(self.minheap) > len(self.maxheap): 
            return float(self.minheap[0])
        if len(self.maxheap) > len(self.minheap): 
            return float(-self.maxheap[0])
        return (-self.maxheap[0] + self.minheap[0])/2


        
        
        