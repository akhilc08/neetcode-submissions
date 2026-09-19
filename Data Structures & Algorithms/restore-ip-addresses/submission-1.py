class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        ip = []
        d = 4

        def back(i,j): 
            if i == j == len(s) and len(ip) == 4: 
                res.append(".".join(ip))
            
            for k in range(j+1,len(s)+1):
                if self.valid(s,i,k): 
                    ip.append(s[i:k])
                    back(k,k)
                    ip.pop()

        back(0,0)
        return res



    
    def valid(self, s, l, r): 
        if s[l] == "0" and l != r-1: return False
        if int(s[l:r]) > 255: return False
        return True
        