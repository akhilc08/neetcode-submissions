class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3: 
            return max(nums)
        return max(self.robList(nums[1:len(nums)]),self.robList(nums[:len(nums)-1]))
        
            
    def robList(self, nums):
        if len(nums)<=2: 
            return max(nums)
        nums[2] += nums[0]
        for i in range(3,len(nums)):
            nums[i]+= max(nums[i-2],nums[i-3])
        
        return max(nums)
