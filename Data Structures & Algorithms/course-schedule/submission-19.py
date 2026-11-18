class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj = [[] for i in range(numCourses)]
        for c1, c2 in prerequisites: 
            adj[c1].append(c2)

        
        visited = set()
        visiting = set()
        def dfs(course): 
            if course in visited: return True
            if course in visiting: return False

            reqs = adj[course]
            visiting.add(course)
            for req in reqs: 
                if not dfs(req): return False

            visiting.remove(course)
            visited.add(course)
            return True


        for i in range(numCourses): 
            if not dfs(i): return False
        
        return True
            

        