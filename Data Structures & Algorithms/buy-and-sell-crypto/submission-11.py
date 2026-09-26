class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        lo, hi = prices[0],prices[0]

        for i in range(len(prices)): 
            new = prices[i]
            if new > hi: 
                hi = new
                res = max(res, hi-lo)
            if new < lo: 
                lo = new
                hi = new
            res = max(hi-lo, res)
        
        return res 
        