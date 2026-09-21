class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        curr = []
        
        def dfs(start):
            if len(curr) == 4: 
                if start == len(s): 
                    res.append(".".join(curr))
                return


            for i in range(start+1,len(s)+1):
                if self.valid(s,start,i): 
                    curr.append(s[start:i])

                    dfs(i)

                    curr.pop()
        dfs(0)
        return res

    def valid(self,s,l,r): 
        if s[l] == "0" and l != r-1: return False
        if int(s[l:r]) > 255: return False
        return True



        