class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        
        def dfs(start, curr, nums): 
            for i in range(start,len(nums)): 
                results.append(curr+[nums[i]])
                dfs(i+1,curr+[nums[i]],nums)

        dfs(0,[],nums)
        return results
        