class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        long = 0
        i = 0
        k = 0
        while i < len(s) and k < len(t): 
            if s[i] == t[k]: 
                temp = 0
                while i<len(s) and k<len(t) and s[i] == t[k]: 
                    long += 1
                    i+=1
                    k+=1
                i-=1


            i+=1
        return len(t) - long
        