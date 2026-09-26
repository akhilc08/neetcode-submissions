class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        if not firstList or not secondList: return []

        i, j = 0,0

        res = []
        
        while i<len(firstList) and j<len(secondList):
            l1, r1 = firstList[i]
            l2, r2 = secondList[j]
            
            lo, hi = max(l1,l2), min(r1,r2)

            if lo<=hi: 
                res.append([lo,hi])

            if r1>r2: 
                j+=1
            elif r2>r1: 
                i+=1
            else: 
                i+=1
                j+=1

            
        return res
