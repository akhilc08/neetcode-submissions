class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c): 
            queue = []
            queue.append((r,c))
            per = 0
            while queue: 
                r,c = queue.pop(0)
                
                if r >= rows or c >= cols or r<0 or c<0 or grid[r][c] == 0: 
                    per+=1
                elif (r,c) in visited: 
                    continue 
                else: 
                    visited.add((r,c))
                    queue.append((r+1,c))
                    queue.append((r-1,c))
                    queue.append((r,c+1))
                    queue.append((r,c-1))
            return per


        for i in range(rows): 
            for j in range(cols): 
                if (i,j) not in visited and grid[i][j] == 1: 
                    return dfs(i,j)