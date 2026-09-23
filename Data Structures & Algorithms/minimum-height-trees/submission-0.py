class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        hmap = defaultdict(list)
        for e1, e2 in edges: 
            hmap[e1].append(e2)
            hmap[e2].append(e1)

        minheight = n
        res = []
        for i in range(n):
            nheight = self.height(hmap, i)
            if nheight == minheight: 
                res.append(i)
            elif nheight < minheight: 
                minheight = nheight
                res = [i]
        return res


        
    def height(self, adj, root): 
        visited = set()

        def dfs(node, h): 
            if node in visited: return -1
            
            visited.add(node)
            high = 0
            for child in adj[node]: 
                height = dfs(child, 1)
                if height > high: 
                    high = height
            
            return high+h
        
        
        return dfs(root, 0)





        