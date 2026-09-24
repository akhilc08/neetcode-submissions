class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        hmap = defaultdict(list)

        for e1, e2 in edges: 
            hmap[e1].append(e2)
            hmap[e2].append(e1)

        visited = set()
        visiting = set()
        
        def dfs(node, parent): 
            if node in visited: return True 
            if node in visiting: return False 

            visiting.add(node)
            for child in hmap[node]: 
                if child != parent: 
                    if not dfs(child, node): return False 
            
            visiting.remove(node)
            visited.add(node)
            return True


        if not dfs(0, -1): return False

        return len(visited) == n

