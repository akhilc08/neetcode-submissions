class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26
        if len(s2)<len(s1): return False
        

        for i,c in enumerate(s1): 
            arr1[ord(c) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1
        
        i = len(s1)
        start = 0
        while (arr1 != arr2) and (i < len(s2)):

            print(arr2)
            arr2[ord(s2[start]) - ord('a')] -= 1
            arr2[ord(s2[i]) - ord('a')] += 1

            start+=1
            i+=1


        return arr1 == arr2



        

        