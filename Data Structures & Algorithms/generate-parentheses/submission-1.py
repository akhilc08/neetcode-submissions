class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        curr = []
        res = []

        def dfs(l,r): 
            if l == r == 0: 
                res.append("".join(curr))
                return
            
            elif l == r:
                curr.append("(") 
                dfs(l-1, r)
                curr.pop()
                return 
            
            elif l < r: 
                if l>0: 
                    curr.append("(") 
                    dfs(l-1, r)
                    curr.pop()
                if r>0: 
                    curr.append(")")
                    dfs(l,r-1)
                    curr.pop()
                return 

        dfs(n,n)
        return res





        