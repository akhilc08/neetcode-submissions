class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1: 
            return -1

        q = deque()
        q.append((0,0))
        res = 1
        visited = set()


        while q: 
            print(q)
            for i in range(len(q)): 
                
                r,c = q.popleft()
                if r>n-1 or c>n-1 or r<0 or c<0 or (r,c) in visited: 
                    print("check1", str((r,c)))
                    continue
                if grid[r][c] == 1: 
                    print("check2", str((r,c)))
                    continue
                
                if r == c == n-1: 
                    return res 

                visited.add((r,c))
                for d1,d2 in directions: 
                    q.append((r+d1,c+d2))
            res+=1
        return -1


                



        