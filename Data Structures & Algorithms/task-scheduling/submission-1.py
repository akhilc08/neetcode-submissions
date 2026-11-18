class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        count = defaultdict(int)
        for task in tasks: 
            count[task]+=1

        heap = []
        for value in count.values(): 
            heap.append(-value)

        heapq.heapify(heap)
        q = deque()

        cycle = 0
        while heap or q: 
            if heap: 
                element = -1*heapq.heappop(heap)
                element -= 1
                if element > 0: 
                    q.append((element, cycle+n))

            while q and q[0][1] == cycle: 
                e = q.popleft()[0]
                heapq.heappush(heap, -1*e)

            cycle += 1
        
        return cycle
        



        
        