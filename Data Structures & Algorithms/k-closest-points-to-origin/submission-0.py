class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance = []

        for x,y in points: 
            d = math.sqrt((x*x + y*y))
            heapq.heappush(distance, (d,(x,y)))

        print(distance)
        res = []
        for i in range(k):
            d,p = heapq.heappop(distance)
            res.append(p)




        return res