class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        print(nums)
        result = []
        def dfs(start, curr, target):
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]: 
                    continue
                if target-nums[i] <0:
                    return 
                if target-nums[i] == 0: 
                    result.append(curr+[nums[i]])

                    return 
                if target-nums[i]>0: 
                    dfs(i+1,curr+[nums[i]],target-nums[i])

        dfs(0,[],target)
        return result
                
        