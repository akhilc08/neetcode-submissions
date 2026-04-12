class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c): 
            print(r,c)
            if r < 0 or c < 0 or r>rows-1 or c > cols-1 or (grid[r][c] == 0) or (r,c) in visited: 
                print("check")
                return 0
            visited.add((r,c))
            return 1+dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)


        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == 1:
                    cur_max = dfs(i,j)
                    res = max(res, cur_max)
                visited.add((i,j))

        return res

        