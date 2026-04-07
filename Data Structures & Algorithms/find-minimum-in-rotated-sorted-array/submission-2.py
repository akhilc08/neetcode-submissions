class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            if r-l <2:
                return min(nums[l],nums[r])
            m = int((l+r)/2)
            print(l,m,r)
            if nums[m]<nums[r]:
                r = m
            else:
                l = m

        if l == r:
            return nums[l]

