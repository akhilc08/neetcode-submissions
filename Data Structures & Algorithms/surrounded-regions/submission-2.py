class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])

        visited = set()
        
        def dfs(r,c): 
            if r>rows-1 or c>cols-1 or r<0 or c<0 or (r,c) in visited: 
                return 
            
            visited.add((r,c))
            print(r,c)
            if board[r][c] == "O": 
                board[r][c] = "T"
                print(r,c,board[r][c])
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            else: 
                return 
        

        for i in range(rows): 
            if board[i][0] == "O": 
                dfs(i,0)
            if board[i][cols-1] == "O":
                dfs(i,cols-1)
        
        for i in range(cols): 
            if board[0][i] == "O": 
                dfs(0,i)
            if board[rows-1][i] == "O":
                dfs(rows-1,i)
        
        for i in range(rows): 
            for j in range(cols):
                if board[i][j] == "O": 
                    board[i][j] = "X"
                elif board[i][j] == "T": 
                    board[i][j] = "O"
        
