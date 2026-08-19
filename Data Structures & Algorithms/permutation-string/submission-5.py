class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a1 = [0] * 26
        a2 = [0] * 26
        if len(s2)<len(s1):
            return False

        for i in range(len(s1)): 
            a1[ord(s1[i]) - ord('a')] +=1
            a2[ord(s2[i]) - ord('a')] +=1


        for i in range(len(s1),len(s2)):
            if a1==a2: 
                return True
        
            a2[ord(s2[i-len(s1)]) - ord('a')] -=1
            a2[ord(s2[i]) - ord('a')] +=1

        if a1==a2: 
            return True
        return False

        


        

        