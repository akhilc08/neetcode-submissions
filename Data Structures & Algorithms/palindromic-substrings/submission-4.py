class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        for i in range(n):
            l = i
            r = i
            while l>-1 and r<n and s[l] == s[r]:
                count += 1
                l-=1
                r+=1

            l = i
            r = i+1
            while l>-1 and r<n and s[l] == s[r]:
                count += 1
                l-=1
                r+=1


        return count
