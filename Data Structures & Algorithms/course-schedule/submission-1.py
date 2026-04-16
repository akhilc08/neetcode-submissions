class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        reqs = defaultdict(list)
        for prereq in prerequisites:
            reqs[prereq[0]].append(prereq[1])

        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting: return False
            if node in visited: return True
            visiting.add(node)
            for neighbor in reqs[node]:
                if not dfs(neighbor): return False
            visiting.remove(node)
            visited.add(node)
            return True

        for req in range(numCourses):
            if not dfs(req): return False
        
        return True