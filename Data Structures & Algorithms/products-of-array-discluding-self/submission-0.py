class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums: 
            if nums.count(0) >1:
                return [0]*len(nums)
            else:
                arr = [0]*len(nums)
                index = nums.index(0)
                nums.remove(0)
                product = 1
                for num in nums:
                    product*=num
                arr[index] = product
                return arr
        else:
            product = 1
            for num in nums: 
                product*=num
            for i, num in enumerate(nums): 
                nums[i] = int(product/num)
            return nums

