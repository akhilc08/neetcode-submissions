class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <2:
            return 0
        
        buy = 0
        sell = 1
        profit = prices[sell]-prices[buy]
        for i in range(1,len(prices)):
            print(prices[i])
            print(prices[buy],prices[sell])
            if prices[buy]> prices[i] and i != len(prices)-1:
                print("check1")
                buy = i
                sell = i+1
                newprofit = prices[sell]-prices[buy]
                profit = newprofit if newprofit>profit else profit
            elif prices[sell]<prices[i]:
                print("check2")
                sell = i
                newprofit = prices[sell]-prices[buy]
                profit = newprofit if newprofit>profit else profit
        return profit if profit > 0 else 0
