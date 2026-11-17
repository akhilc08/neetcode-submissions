class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r,c): 
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited: return 

            visited.add((r,c))

            if grid[r][c] == "1": 

                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        
        islands = 0
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == "1" and (i,j) not in visited: 
                    islands +=1 
                    dfs(i,j)
        
        return islands 
