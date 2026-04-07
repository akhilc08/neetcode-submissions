class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        if len(s) != len(t): 
            return False
        for i in range (0,len(s)):
            if s[i] in smap: 
                smap[s[i]] += 1
            else:
                smap[s[i]] = 1
            if t[i] in tmap:
                tmap[t[i]] += 1
            else: 
                tmap[t[i]] = 1

        print(smap)
        print(tmap)

        return smap == tmap