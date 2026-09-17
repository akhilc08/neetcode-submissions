class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def dfs(co, cc, curr, n):
            if co == n:
                c_temp = curr
                while cc < n:
                    c_temp += ")"
                    cc += 1
                results.append(c_temp)
                return
            elif co == cc: 
                print(co,cc,curr,n)
                dfs(co+1,cc,curr+"(",n)
            elif co >cc: 
                print(co,cc,curr,n)
                dfs(co+1,cc,curr+"(",n)
                dfs(co,cc+1,curr+")",n) 

            else: 
                return
        
        dfs(0,0,"",n)
        return results

        