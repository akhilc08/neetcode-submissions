class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1], [-1,0], [0,-1]]

        res = -1

        visited = set()
        def dfs(r,c): 

            if r>rows-1 or c>cols-1 or r<0 or c<0 or (r,c) in visited or grid[r][c] == 0: 
                return []
            visited.add((r,c))
            grid[r][c] = 2

            return [(r,c)] + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c+1) + dfs(r,c-1)

        def bfs(r,c): 
            nonlocal res 
            q = deque()
            for cords in dfs(r,c): 
                q.append(cords)

            print(q)
            while q: 
                for i in range(len(q)): 
                    r1,c1 = q.popleft()

                    if r1>rows-1 or c1>cols-1 or r1<0 or c1<0 or grid[r1][c1] == 3: continue

                    if grid[r1][c1] == 1: 
                        return res
                    else: 
                        grid[r1][c1] = 3
                        for d1, d2 in directions: 
                            q.append((r1+d1, c1+d2))
                
                res+=1
            return res
        
        for i in range(rows):
            for j in range(cols): 
                if grid[i][j] == 1: 
                    return bfs(i,j)