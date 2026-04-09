class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        visited = set()

        def dfs(r,c,i):
            if i == (len(word)):
                return True
            if (r<0 or c<0 or r>rows-1 or c>cols-1 or ((r,c) in visited)):
                return False
            
            if board[r][c] == word[i]:
                visited.add((r,c))
                found = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1)
                visited.remove((r,c))
                return found
            
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0): return True

        return False
            
            
            


      