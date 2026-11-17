class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        sets = []
        res = []
        total = 0

        def dfs(start, target): 
            if target == 0: 
                sets.append(res.copy())
                return 
            if target < 0: return 

            for i in range(start, len(nums)): 
                res.append(nums[i])

                dfs(i, target-nums[i])

                res.remove(nums[i])

            
        dfs(0,target)
        return sets
            

