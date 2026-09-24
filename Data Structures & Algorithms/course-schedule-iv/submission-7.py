class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:


        rmap = defaultdict(set)

        for c1, c2 in prerequisites: 
            rmap[c2].add(c1)

        visited = set()
        def dfs(node): 
            if node in visited: return rmap[node]

            children = rmap[node].copy()
            for child in children: 
                rmap[node] |= dfs(child)

            visited.add(node)
            return rmap[node]
            

        
        for i in range(numCourses): 
            dfs(i)
        
        res = []
        for q1, q2 in queries: 
            if q1 in rmap[q2]: res.append(True)
            else: res.append(False)

        return res


        
