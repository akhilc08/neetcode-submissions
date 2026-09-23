class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        if not nums: return 0
        res = 0

        def dfs(start, curr):
            nonlocal res

            for i in range(start,len(nums)): 
                res += (curr ^ nums[i])

                dfs(i+1, curr^nums[i])

        dfs(0,0)
        return res



