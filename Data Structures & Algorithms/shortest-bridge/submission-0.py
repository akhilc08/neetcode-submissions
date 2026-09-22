class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)
        res = -2
        dfs_visited = set()
        island = []

        def dfs(r,c): 
            
            if r>n-1 or c>n-1 or r<0 or c<0 or (r,c) in dfs_visited: 
                return
            
            dfs_visited.add((r,c))

            if grid[r][c] == 1: 
                island.append((r,c))
                grid[r][c] = 2
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)


        def bfs(r,c): 
            nonlocal res
            dfs(r,c)
            q = deque()
            for cords in island: 
                q.append(cords)
            
            while q: 
                print(q)
                res+=1
                for i in range(len(q)): 
                    r1,c1 = q.popleft()
                    if r1>n-1 or c1>n-1 or r1<0 or c1<0: 
                        continue
                    if grid[r1][c1] == 1: 
                        return res
                    elif grid[r1][c1] == 0 or grid[r1][c1] == 2: 
                        grid[r1][c1] = 3
                        q.append((r1+1,c1))
                        q.append((r1-1,c1))
                        q.append((r1,c1+1))
                        q.append((r1,c1-1))

        for i in range(n): 
            for j in range(n): 
                if grid[i][j] == 1: 
                    bfs(i,j)
                    return res


        