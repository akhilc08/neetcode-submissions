class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = [0] * (len(prices)+1)
        cache[len(prices)-1] = 0
        for i in range(len(prices)-2,-1,-1): 

            high = 0
            for j in range(i+1, len(prices)): 
                high = max(high, prices[j]-prices[i] + cache[j+1], )

            cache[i] = max(high, cache[i+1])

        return cache[0]




        