class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3: return max(nums)
        
        rob = [0]*len(nums)
        rob[0] = nums[0]
        rob[1] = max(nums[1], nums[0])

        for i in range(2,len(nums)): 
            rob[i] = max(rob[i-1], nums[i]+rob[i-2])
        
        return rob[len(nums)-1]

