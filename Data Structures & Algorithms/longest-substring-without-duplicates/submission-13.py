class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        i = 0
        seen = set()
        for j, c in enumerate(s): 

            while c in seen: 
                seen.remove(s[i])
                i+=1
            res = max(res, j-i+1) 
            seen.add(c)


        return res
        