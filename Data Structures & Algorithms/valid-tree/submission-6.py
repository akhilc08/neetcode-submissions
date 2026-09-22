class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        hmap = defaultdict(list)
        for e1, e2 in edges: 
            hmap[e1].append(e2)
            hmap[e2].append(e1)


        visiting = set() 

        def dfs(node,prev):
            if node in visiting: return False

            visiting.add(node)
            for child in hmap[node]: 
                if child != prev: 
                    if not dfs(child,node): return False
            
            return True


        

        if not dfs(0,-1): return False

        return len(visiting) == n