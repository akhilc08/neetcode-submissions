class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        
        long_idx = [0,0]
        long_len = 0

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j-i<3 or dp[i+1][j-1] == True:
                        dp[i][j] = True

                        if j-i > long_len:
                            long_len = j-i
                            long_idx[0] = i
                            long_idx[1] = j
        
        return s[long_idx[0]:long_idx[1]+1]


        