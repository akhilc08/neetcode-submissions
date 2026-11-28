class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def isPossible(k): 
            count = 0
            i = 0
            while i<len(piles): 
                eaten = 0
                count += (piles[i] + k - 1) // k
                i+=1
                if count > h: return False
            
            return True
        
        low = 1
        high = max(piles)


        while low < high: 

            m = (high + low) // 2
            if isPossible(m): 
                high = m
            else: 
                low = m+1
        
        return low


        