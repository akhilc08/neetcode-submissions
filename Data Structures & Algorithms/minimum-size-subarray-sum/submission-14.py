class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i, j = 0,0
        total = 0
        res = len(nums)+1

        while j <= len(nums): 
            print(i,j,res,total)

            if total > target or total == target: 
                res = min(res,j-i)
                total -= nums[i]
                i+=1

            elif total< target: 
                if j < len(nums): 
                    total += nums[j]
                j+=1



        
        return res if res != len(nums)+1 else 0