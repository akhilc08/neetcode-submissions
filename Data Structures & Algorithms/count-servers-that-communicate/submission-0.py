class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        res = 0

        def check(r,c): 
            nonlocal res
            
            found = False
            r1 = r+1
            while r1<rows: 
                if grid[r1][c] == 1: 
                    found = True
                    grid[r1][c] = 2
                    res+=1
                if grid[r1][c] == 2: 
                    found = True
                r1+=1

            r1 = r-1
            while r1>-1: 
                if grid[r1][c] == 1: 
                    found = True
                    grid[r1][c] = 2
                    res+=1
                if grid[r1][c] == 2: 
                    found = True
                r1-=1
            
            c1 = c+1
            while c1<cols: 
                if grid[r][c1] == 1: 
                    found = True
                    grid[r][c1] = 2
                    res+=1
                if grid[r][c1] == 2: 
                    found = True
                c1+=1

            c1 = c-1
            while c1>-1: 
                if grid[r][c1] == 1: 
                    found = True
                    grid[r][c1] = 2
                    res+=1
                if grid[r][c1] == 2: 
                    found = True
                c1-=1


            if found: 
                grid[r][c] = 2
                res+=1
        
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 1: 
                    check(i,j)

        return res