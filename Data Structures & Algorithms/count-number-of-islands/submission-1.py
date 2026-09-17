class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        

        def dfs(r,c): 
            if r+1 < rows and (r+1,c) not in visited: 
                visited.add((r+1,c))
                if grid[r+1][c] == "1": 
                    dfs(r+1,c)
            
            if c+1 < cols and (r,c+1) not in visited: 
                visited.add((r,c+1))
                if grid[r][c+1] == "1": 
                    dfs(r,c+1)
                

            if r-1 > -1 and (r-1, c) not in visited: 
                visited.add((r-1,c))
                if grid[r-1][c] == "1": 
                    dfs(r-1,c)
            
            if c-1 > -1 and (r,c-1) not in visited: 
                visited.add((r,c-1))
                if grid[r][c-1] == "1": 
                    dfs(r,c-1)



        
        result = 0
        for i in range(0,rows): 
            for j in range(0,cols):
                if (i,j) not in visited: 
                    if grid[i][j] == "1": 
                        dfs(i,j)
                        print(i,j)
                        result+=1
                    visited.add((i,j))

        return result





