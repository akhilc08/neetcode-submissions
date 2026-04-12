class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = nums[0]
        window = 100000
        l = 0
        r = 1
        while r<len(nums):

            if total<target:
                total+=nums[r]
                r+=1
            else: 
                window = min(window, r-l)
                total-=nums[l]
                l+=1

        while total >= target and l<len(nums):
            window = min(window, r-l)
            total-=nums[l]
            l+=1

        return 0 if window >len(nums) else window

