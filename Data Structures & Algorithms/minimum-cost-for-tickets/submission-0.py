class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        
        memo = [-1]* len(days)

        def dfs(start): 
            if start == len(days): 
                return 0
            if memo[start] != -1: return memo[start]
            
            one = costs[0] + dfs(start+1)
            
            start2 = start
            while start2 < len(days) and days[start2] < days[start]+7:
                start2+=1
            
            two = dfs(start2) + costs[1]

            start3 = start
            while start3 < len(days) and days[start3] < days[start]+30: 
                start3+=1
            three = dfs(start3) + costs[2]

            memo[start] = min(one, two, three)
            return memo[start]

        dfs(0)
        print(memo)
        return memo[0]



        