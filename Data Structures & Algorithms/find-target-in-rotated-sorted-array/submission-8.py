class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        min = self.minSearch(nums)
        min_index = nums.index(min)
        if min == target: 
            print("check3")
            return min_index
        elif min <= target <= nums[len(nums)-1]:
            print("check1")
            return min_index+self.binSearch(nums[min_index:len(nums)], target) if self.binSearch(nums[min_index:len(nums)], target) != -1 else -1
        elif nums[0] <= target <= nums[min_index-1]:
            print("check2")
            return self.binSearch(nums[0:min_index], target)
        else: 
            return -1

    def binSearch(self, nums, target):

        if len(nums) == 1 and nums[0] != target:
            return -1

        mid = int(len(nums)/2)
        left = nums[:mid]
        right = nums[mid:]
        if target == nums[mid]:
            return mid
        elif target <nums[mid]:
            return self.binSearch(left,target)
        else: 
            return mid+self.binSearch(right,target) if self.binSearch(right,target) != -1 else -1

    def minSearch(self, nums): 
        if len(nums)<3:
            return min(nums)

        mid = int(len(nums)/2)

        if self.increasing(nums[mid-1],nums[mid],nums[mid+1]):
            left = nums[:mid]
            right = nums[mid:]
            return min(self.minSearch(left),self.minSearch(right))
        else:
            return min(nums[mid],nums[mid+1])
        
    def increasing(self,i, j, k):
        return i<j<k