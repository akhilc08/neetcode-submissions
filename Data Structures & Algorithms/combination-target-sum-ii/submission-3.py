class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        sets = []
        res = []

        def dfs(start, target): 
            if target == 0: 
                sets.append(res.copy())
                return

            if target < 0: return 

            for i in range(start, len(candidates)): 

                if start != i  and candidates[i] == candidates[i-1]: 
                    continue 

                res.append(candidates[i])

                dfs(i+1, target-candidates[i])

                res.remove(candidates[i])
        
        dfs(0,target)
        return sets