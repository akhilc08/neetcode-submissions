class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        used = {}
        cmax = 0
        start = 0
        end = 0

        for i, char in enumerate(s): 

            if char in used: 
                start = max(start, used[char]+1)


            end = i
            print(i,start,end,cmax)
            cmax = max(cmax,end-start)
            used[char] = i
        print(cmax)
        return cmax+1

