class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])


        def bfs(rotten):
            mins = 0
            while rotten: 
                tile = rotten.popleft()
                i,j = tile[1]
                priority = tile[0]

                if i<0 or j<0 or i>rows-1 or j>cols-1 or grid[i][j] == 0: 
                    continue
                elif grid[i][j] == 1: 
                    rotten.append((priority+1,(i+1,j)))
                    rotten.append((priority+1,(i-1,j)))
                    rotten.append((priority+1,(i,j+1)))
                    rotten.append((priority+1,(i,j-1)))

                    grid[i][j] = 2
                    mins=priority
            return mins




        rotten = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2: 
                    rotten.append((1,(i+1,j)))
                    rotten.append((1,(i-1,j)))
                    rotten.append((1,(i,j+1)))
                    rotten.append((1,(i,j-1)))

        print(rotten)
        res = bfs(rotten)
        print(grid)
        return res if not any( 1 in row for row in grid) else -1

