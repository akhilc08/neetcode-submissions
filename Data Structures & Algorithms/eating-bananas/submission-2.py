class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def isPossible(k): 
            count = 0
            for p in piles: 
                count += (p + k - 1) // k
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


        