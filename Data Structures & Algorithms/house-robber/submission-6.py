class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3: return max(nums)
        
        rob = [0]*len(nums)
        rob[0] = nums[0]
        rob[1] = nums[1]
        rob[2] = max(rob[1], nums[2]+rob[0])
        print(rob,nums)

        for i in range(3,len(nums)): 
            rob[i] = max(rob[i-1], nums[i]+rob[i-2], nums[i]+rob[i-3])
        
        return rob[len(nums)-1]

