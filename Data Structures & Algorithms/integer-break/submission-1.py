class Solution:
    def integerBreak(self, n: int) -> int:

        # 4 : 2,2 
        # 12 : 3,3,3,3  6,6  3,3,6  4,4,4
        
        # max( 12-2 : 10 *2 
        # 10-2 : 8
        # 12-3 : 9 * 3 
        # 12-4: 8 * 4)

        if n == 2: return 1
        if n == 3: return 2
        cache = {}
        cache[2] = 2
        cache[3] = 3

        def dfs(target): 
            if target in cache: return cache[target]

            res = 0
            for i in range(2,target-1): 
                res = max(res, i*dfs(target-i))

            cache[target] = res
            return res

        return dfs(n)

        