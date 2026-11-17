class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        sets = [[]]
        res = []
        def dfs(start): 

            for i in range(start, len(nums)): 
                res.append(nums[i])
                sets.append(res.copy())

                dfs(i+1)

                res.remove(nums[i])
        dfs(0)
        return sets
        