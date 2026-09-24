class Solution:
    def longestPalindrome(self, s: str) -> str:
         
        n = len(s)
        hmap = [[False] * n for _ in range(n)]
        long = 1
        longidx = 0

        for i in range(n-1, -1, -1): 
            for j in range(n-1, i, -1): 

                if s[i] == s[j] and (j-i < 3 or hmap[i+1][j-1] == True): 
                    if j-i+1 > long: 
                        long = j-i+1
                        longidx = i
                    hmap[i][j] = True

                
        return s[longidx:longidx+long]

        
        