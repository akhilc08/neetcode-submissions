class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        cmap = defaultdict(list)
        for i in range(len(isConnected)): 
            for j in range(len(isConnected)): 
                if isConnected[i][j] == 1: 
                    cmap[i].append(j)
                    cmap[j].append(i)

        print(cmap)
        
        visited = set()
        def dfs(node): 
            print(node)
            if node in visited: return 
            visited.add(node)
            for child in cmap[node]: 
                dfs(child)

        res = 0
        for i in range(len(isConnected)): 
            if i not in visited: 
                res+=1
                dfs(i)
        return res


        