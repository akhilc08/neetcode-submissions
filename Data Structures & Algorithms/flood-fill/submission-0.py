class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows, cols = len(image), len(image[0])


        visited = set()
        initial = image[sr][sc]
        def dfs(r,c):
            if r>rows-1 or c> cols-1 or r<0 or c<0 or (r,c) in visited: return

            visited.add((r,c))
            if image[r][c] == initial: 
                image[r][c] = color
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        
        dfs(sr,sc)


        return image