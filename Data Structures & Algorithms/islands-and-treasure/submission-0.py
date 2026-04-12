class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        visited = set()

        def bfs(gates): 

            com = """if r < 0 or c < 0 or r > rows-1 or c > cols-1 or grid[r][c] == -1: 
                return INF
            if grid[r][c] == 0: 
                return 0
            if (r,c) in visited: 
                return grid[r][c]
            else: 
                visited.add((r,c))
                grid[r][c] = 1+min(bfs(r+1,c),bfs(r-1,c),bfs(r,c+1),bfs(r,c-1))
                if grid[r][c] >= INF: 
                    return INF
                return grid[r][c]
            """
            queue = collections.deque()
            for gate in gates: 
                queue.append((0,gate))
            
            while queue: 
                tile = queue.popleft()
                r,c = tile[1]
                if r < 0 or c < 0 or r > rows-1 or c > cols-1 or grid[r][c] == -1:
                    continue
                elif tile[1] not in visited: 
                    grid[r][c] = tile[0]
                    visited.add((r,c))
                    queue.append((tile[0]+1, (r+1,c)))
                    queue.append((tile[0]+1, (r-1,c)))
                    queue.append((tile[0]+1, (r,c+1)))
                    queue.append((tile[0]+1, (r,c-1)))
            
        gates = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0: 
                    gates.append((i,j))
        bfs(gates)

        return None
