class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # 1 2 3 : 4 

        # 1 2 3 : 2

        # 1 2 3 : 3 -> 4
        # 1 2 3 : 2 -> 2
        # 1 2 3 : 1 -> 1 

        cache = {}

        def dfs(target): 
            if target == 0: return 1
            if target in cache: return cache[target]

            res = 0
            for num in nums: 
                if target-num >= 0: 
                    res += dfs(target-num)
            
            cache[target] = res
            return res

        return dfs(target)

        