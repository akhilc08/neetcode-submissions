class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = defaultdict(list)
        for c1,c2 in prerequisites: 
            reqs[c1].append(c2)

        
        visited = set()
        visiting = set()

        def dfs(node): 
            if node in visited: return True
            if node in visiting: return False

            visiting.add(node)
            for child in reqs[node]: 
                if not dfs(child): return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses): 
            if not dfs(i): return False
        return True

