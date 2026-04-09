class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()

        def bfs(i,j):
            if i>rows-1 or j>cols-1 or i<0 or j<0 or (i,j) in visited: 
                return 
            visited.add((i,j))
            if grid[i][j] == "1":
                bfs(i-1,j)
                bfs(i+1,j)
                bfs(i,j-1)
                bfs(i,j+1)
            else: 
                return
            
            

        output = 0

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited: 
                    if grid[i][j] == '0': 
                        visited.add((i,j))
                    else: 
                        bfs(i,j)
                        print(i,j)
                        output+=1

        return output




