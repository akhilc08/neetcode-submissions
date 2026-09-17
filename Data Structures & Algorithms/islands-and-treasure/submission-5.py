class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        

        def bfs(t): 

            q = collections.deque()
            visited = set()
            for c in t: 
                q.append((0,c))
            
            while q: 

                d, c = q.popleft()

                i,j = c



                if i>rows-1 or j>cols-1 or i<0 or j<0 or grid[i][j] == -1 or (i,j) in visited:
                    continue
                visited.add(c)

                if grid[i][j] > d: 

                    grid[i][j] = d

                q.append((d+1,(i+1,j)))
                q.append((d+1,(i,j+1)))
                q.append((d+1,(i-1,j)))
                q.append((d+1,(i,j-1)))

        t = []
        for i in range(rows): 
            for j in range(cols):
                if grid[i][j] == 0: 
                    t.append((i,j))

        bfs(t)
                