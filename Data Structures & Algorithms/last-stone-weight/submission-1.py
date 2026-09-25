class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        maxheap = []
        if len(stones) == 1: return stones[0]

        for stone in stones: 
            heapq.heappush(maxheap, -stone)

        while maxheap: 
            s1, s2 = -heapq.heappop(maxheap), -heapq.heappop(maxheap)

            if s1 > s2: 
                s1-=s2
                heapq.heappush(maxheap, -s1)
            if len(maxheap) == 1: 
                return -maxheap[0]
        return 0
        