class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        

        def dfs(r,c): 
            if r>rows-1 or c>cols-1 or c<0 or r<0 or (r,c) in visited: 
                return 
            
            visited.add((r,c))
            if grid[r][c] == "1":
                dfs(r+1,c)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r,c-1)




        
        result = 0
        for i in range(rows): 
            for j in range(cols):
                if (i,j) not in visited: 
                    if grid[i][j] == "1": 
                        dfs(i,j)
                        print(i,j)
                        result+=1
                    visited.add((i,j))

        return result





