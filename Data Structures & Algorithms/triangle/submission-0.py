class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        cache = {}
        rows = len(triangle)

        def dfs(r,c): 
            cols = len(triangle[r])
            if r>rows-1 or c>cols-1 or r<0 or c<0: return math.inf
            if r == rows-1: return triangle[r][c]
            if (r,c) in cache: return cache[(r,c)]

            cache[(r,c)] = triangle[r][c] + min(dfs(r+1, c), dfs(r+1, c+1))

            return cache[(r,c)]
        
        dfs(0,0)
        print(cache)
        return dfs(0,0)



        