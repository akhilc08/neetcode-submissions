class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]

        high = [0]*len(nums)
        high[0] = nums[0]
        high[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)): 
            high[i] = max(high[i-1], nums[i] + high[i-2])
        
        return high[-1]

        