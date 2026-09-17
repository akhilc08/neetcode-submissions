class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)
        result = []
        def dfs(start, curr, target): 
            
            for i in range(start,len(nums)):
                if target-nums[i]<0: 
                    return
                elif target-nums[i]==0:
                    result.append(curr+[nums[i]])
                    return
                else: 
                    
                    dfs(i,curr+[nums[i]],target-nums[i])
        
        dfs(0,[],target)
        return result

                
            
            

