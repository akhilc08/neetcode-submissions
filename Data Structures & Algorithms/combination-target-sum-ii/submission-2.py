class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        nums = sorted(candidates)
        print(nums)
        res = []
        curr = []
        def back(start, target):

            for i in range(start,len(nums)): 
                if i>start and nums[i] == nums[i-1]: 
                    continue
                
                if target-nums[i] <0: 
                    return 
                if target-nums[i] == 0: 
                    curr.append(nums[i])
                    print(curr)
                    res.append(curr.copy())
                    curr.pop()
                    return 
                if target-nums[i] > 0: 
                    curr.append(nums[i])
                    back(i+1, target-nums[i])
                    curr.pop()

        back(0,target)
        return res

