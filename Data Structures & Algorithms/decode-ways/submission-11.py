class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0


        dp = [-1]* len(s)
        def dfs(start): 
            if start >= len(s): return 1
            if dp[start] != -1: return dp[start]

            print(start)

            res = 0
            c1 = s[start]
            if int(c1) > 0: 
                print("check")
                res+= (dfs(start+1))

            if not (start+2 > len(s)):
                c2 = s[start:start+2]
                if c2[0] != "0" and int(c2) > 0 and int(c2) <27: 
                    res += (dfs(start+2))
                    print(res)
            print(dp)
            print(res)
            dp[start] = res
            return res
        
        return dfs(0)

