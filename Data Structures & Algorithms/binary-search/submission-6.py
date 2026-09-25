class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bsearch(nums, target, l, r):

            if l>r: return -1 
            m = ((r-l)//2)+l

            if target == nums[m]: 
                return m
            if target<nums[m]: 
                return bsearch(nums,target,l,m-1)
            if target>nums[m]: 
                return bsearch(nums,target,m+1,r)
            
        return bsearch(nums,target, 0, len(nums)-1)
        