class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        visited = {}

        def dfs(start): 
            if start in visited: return visited[start]
            if start == len(s): 
                return True


            for i in range(start,len(s)+1): 
                if s[start:i] in wordDict: 
                    visited[start] = dfs(i)
                    if visited[start]: return True
            
            return False

        return dfs(0)



        