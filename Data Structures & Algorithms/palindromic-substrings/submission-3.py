class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        dp = [[False]*n for i in range(n)]
        
        for i in range(n):
            for j in range(i):
                if s[i] == s[j] and (i-j<3 or dp[j+1][i-1]):
                    count+=1
                    dp[j][i] = True

        return count+len(s)
