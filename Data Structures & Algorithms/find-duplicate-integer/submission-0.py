class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        i = 0
        while nums[i] != -1: 
            temp = nums[i]
            nums[i] = -1
            i = temp
        
        return i 
        