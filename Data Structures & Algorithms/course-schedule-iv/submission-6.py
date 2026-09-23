class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

        reqs = defaultdict(list)
        for r1, r2 in prerequisites: 
            reqs[r2].append(r1)
        


        r_map = {}

        def dfs(node): 

            if node in r_map: 
                return r_map[node]
            

            ancestors = set()
            for child in reqs[node]: 
                ancestors.add(child)
                
                ancestors |= dfs(child)
            
            r_map[node] = ancestors
            return ancestors
            



        
        for i in range(numCourses): 
            if i not in r_map: 
                dfs(i)

        res = []
        for q1,q2 in queries: 
            if q1 in r_map[q2]: 
                res.append(True)
            else: 
                res.append(False)

        return res