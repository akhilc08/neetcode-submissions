class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        q = deque()
        heapq.heapify(heap)

        t = 0

        while heap or q: 
            if heap: 
                c = 1+heapq.heappop(heap)
                if c != 0: 
                    q.append((c, t+n ))

            while q and q[0][1] == t: 
                heapq.heappush(heap, q.popleft()[0])
            t+=1

        return t




        