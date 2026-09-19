class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        def back(i,j, curr): 
            if i == j == len(s):
                res.append(curr) 
            
            for k in range(j,len(s)):
                if self.isPali(s,i,k): 
                    curr_c = curr.copy()
                    curr_c.append(s[i:k+1])
                    back(k+1,k+1,curr_c)
                

        back(0,0,[])
        return(res)


    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True