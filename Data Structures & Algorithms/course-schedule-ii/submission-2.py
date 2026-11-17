class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indeg = [0]*numCourses
        adj = [[] for i in range(numCourses)]

        for c1, c2 in prerequisites: 
            indeg[c2]+=1
            adj[c1].append(c2)

        q = deque()
        for i in range(numCourses): 
            if indeg[i] == 0: 
                q.append(i)

        res = []
        while q: 
            node = q.popleft()
            res.append(node)

            for nodes in adj[node]: 
                indeg[nodes] -=1

                if indeg[nodes] == 0: 
                    q.append(nodes)

        if len(res) != numCourses: return []
        return res[::-1]


        