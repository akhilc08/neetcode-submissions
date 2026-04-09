class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        result = []

        def backtrack(start, target, path):
            for i in range(start,len(nums)): 
                if target-nums[i] < 0:
                    return
                elif target-nums[i] == 0: 
                    result.append(path + [nums[i]])
                    return
                else:
                    backtrack(i, target-nums[i], path + [nums[i]])


        backtrack(0, target, [])

        return result