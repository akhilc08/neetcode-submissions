class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        results = [[]]
        nums.sort()

        def dfs(start, curr): 
            
            for i in range(start,len(nums)): 

                if i>start and nums[i] == nums[i-1]: 
                    continue
                
                results.append(curr+[nums[i]])
                dfs(i+1, curr+[nums[i]])

        dfs(0,[])
        return results
