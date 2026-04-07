class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<3:
            return min(nums)

        mid = int(len(nums)/2)

        if self.increasing(nums[mid-1],nums[mid],nums[mid+1]):
            left = nums[:mid]
            right = nums[mid:]
            return min(self.findMin(left),self.findMin(right))
        else:
            return min(nums[mid],nums[mid+1])
        
    def increasing(self,i, j, k):
        return i<j<k