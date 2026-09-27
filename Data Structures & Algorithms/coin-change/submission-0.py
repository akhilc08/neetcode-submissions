class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        res = math.inf

        def dfs(remaining): 

            if remaining in cache: return cache[remaining]
            if remaining < 0: return math.inf
            res = math.inf
            if remaining == 0: res = 0
            else: res = 1+min(dfs(remaining - c) for c in coins)
            
            cache[remaining] = res
            return res
        
        ans = dfs(amount)
        return ans if ans != math.inf else -1

            

        