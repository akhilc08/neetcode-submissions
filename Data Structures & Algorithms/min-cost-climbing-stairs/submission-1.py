class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [0]*(len(cost))
        for i in range(len(cost)): 
            if i == 0 or i == 1: 
                mincost[i] = cost[i]
            else: 
                mincost[i] = cost[i]+min(mincost[i-1],mincost[i-2])
        
        print(mincost)
        
        return min(mincost[len(cost)-1], mincost[len(cost)-2])
